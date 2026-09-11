/**
 * Obsidian Vault Wikilink & Markdown Integrity Validator (Node.js ESM)
 * Runs on Node.js v22 without external dependencies.
 */

import fs from 'fs';
import path from 'path';

export function validateVault(vaultRoot = 'D:\\obsidian file', ignoredDirs = ['.agents', '.antigravity', '.git', '.obsidian']) {
  const indexedFiles = new Set();
  const fileList = [];

  function walk(currentDir) {
    const entries = fs.readdirSync(currentDir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.isDirectory()) {
        if (!ignoredDirs.includes(entry.name)) {
          walk(path.join(currentDir, entry.name));
        }
      } else {
        const fullPath = path.join(currentDir, entry.name);
        const relPath = path.relative(vaultRoot, fullPath).replace(/\\/g, '/');
        const ext = path.extname(entry.name);
        const baseName = path.basename(entry.name, ext);
        const relNoExt = relPath.slice(0, -ext.length || undefined);

        indexedFiles.add(entry.name.toLowerCase());
        indexedFiles.add(baseName.toLowerCase());
        indexedFiles.add(relPath.toLowerCase());
        indexedFiles.add(relNoExt.toLowerCase());

        if (entry.name.endsWith('.md')) {
          fileList.push({ fullPath, relPath });
        }
      }
    }
  }

  walk(vaultRoot);

  const wikilinkRegex = /!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]/g;
  const brokenLinks = [];
  const syntaxErrors = [];
  let totalLinks = 0;

  for (const { fullPath, relPath } of fileList) {
    const content = fs.readFileSync(fullPath, 'utf8');
    const lines = content.split(/\r?\n/);

    // Frontmatter validation
    if (content.startsWith('---')) {
      const parts = content.split('---');
      if (parts.length < 3) {
        syntaxErrors.push({ relPath, line: 1, message: 'Unclosed YAML frontmatter' });
      }
    }

    // Code fence balance check
    const fenceCount = lines.filter(line => line.trim().startsWith('```')).length;
    if (fenceCount % 2 !== 0) {
      syntaxErrors.push({ relPath, line: lines.length, message: `Unclosed code fence (odd number: ${fenceCount})` });
    }

    // Wikilink check
    lines.forEach((line, index) => {
      const lineNum = index + 1;
      let match;
      while ((match = wikilinkRegex.exec(line)) !== null) {
        const target = match[1].trim();
        if (target === '...' || !target) continue;
        totalLinks++;
        const normTarget = target.replace(/\\/g, '/').replace(/\/$/, '').toLowerCase();
        if (!indexedFiles.has(normTarget)) {
          brokenLinks.push({ relPath, line: lineNum, target });
        }
      }
    });
  }

  return {
    scannedFiles: fileList.length,
    indexedTargets: indexedFiles.size,
    totalLinks,
    brokenLinks,
    syntaxErrors,
  };
}

if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(decodeURI(new URL(import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, '$1')))) {
  const vaultPath = process.argv[2] || 'D:\\obsidian file';
  console.log(`[Node.js v22 Validator] Scanning: ${vaultPath}`);
  const results = validateVault(vaultPath);
  console.log(`Scanned Markdown Files: ${results.scannedFiles}`);
  console.log(`Total Wikilinks Checked: ${results.totalLinks}`);
  console.log(`Broken Links Found: ${results.brokenLinks.length}`);
  results.brokenLinks.forEach(b => console.log(`  [BROKEN] ${b.relPath}:${b.line} -> [[${b.target}]]`));
  console.log(`Syntax Errors Found: ${results.syntaxErrors.length}`);
  results.syntaxErrors.forEach(s => console.log(`  [SYNTAX] ${s.relPath}:${s.line} -> ${s.message}`));
}
