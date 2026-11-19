const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

function encryptRSIE1(plaintext, password, iterations = 100000) {
  const magic = Buffer.from('RSIE1', 'utf8');
  const salt = crypto.randomBytes(16);
  const iv = crypto.randomBytes(12);

  const key = crypto.pbkdf2Sync(password, salt, iterations, 32, 'sha256');
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  
  const enc1 = cipher.update(Buffer.from(plaintext, 'utf8'));
  const enc2 = cipher.final();
  const enc = Buffer.concat([enc1, enc2]);
  const tag = cipher.getAuthTag();

  // Combine into single buffer
  const total = Buffer.concat([magic, salt, iv, enc, tag]);
  return total.toString('base64');
}

// Read index.html
const rsiDir = path.resolve(__dirname, '..');
const indexPath = path.join(rsiDir, 'index.html');
const rawHtml = fs.readFileSync(indexPath, 'utf8');

// Backup original index.html
const backupPath = path.join(rsiDir, 'index_raw_backup.html');
if (!fs.existsSync(backupPath)) {
  fs.writeFileSync(backupPath, rawHtml, 'utf8');
  console.log('Backed up index.html -> index_raw_backup.html');
}

// Split into Head and Body
const bodyStartMatch = rawHtml.match(/<body[^>]*>/i);
const bodyEndMatch = rawHtml.match(/<\/body>/i);

if (!bodyStartMatch || !bodyEndMatch) {
  console.error('Could not find <body> tags');
  process.exit(1);
}

const bodyStartIdx = bodyStartMatch.index + bodyStartMatch[0].length;
const bodyEndIdx = bodyEndMatch.index;

const headAndPrefix = rawHtml.slice(0, bodyStartIdx);
const innerBody = rawHtml.slice(bodyStartIdx, bodyEndIdx);
const suffix = rawHtml.slice(bodyEndIdx);

console.log('Inner body length:', innerBody.length, 'bytes');

// Encrypt innerBody with standard passkey RSI2027
const ciphertext = encryptRSIE1(innerBody, 'RSI2027');
console.log('Ciphertext base64 length:', ciphertext.length);

// Build new HTML
let newHead = headAndPrefix;
// Inject gatekeeper CSS if not present
if (!newHead.includes('rsi-gatekeeper.css')) {
  newHead = newHead.replace(/<\/head>/i, '  <link rel="stylesheet" href="assets/rsi-gatekeeper.css">\n</head>');
}

const newHtml = `${newHead}
  <!-- RSI Group 2027 Project Hive Confidentially Protected Mount -->
  <div id="rsi-app-mount"></div>
  <script type="application/rsi-payload" id="rsi-encrypted-payload">
${ciphertext}
  </script>
  <script src="assets/rsi-gatekeeper.js"></script>
${suffix}`;

const testOutPath = path.join(rsiDir, 'index_encrypted_test.html');
fs.writeFileSync(testOutPath, newHtml, 'utf8');
console.log('Wrote index_encrypted_test.html successfully!');
