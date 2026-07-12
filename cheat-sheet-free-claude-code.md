# Claude Code Free Setup Cheat Sheet

Quick reference for setting up Claude Code with OpenCode's free API endpoint.

## What is OpenCode?

OpenCode is an AI-powered coding assistant CLI tool that helps with software engineering tasks. It uses various LLM providers including Anthropic Claude.

**Website**: https://opencode.ai/

## What is Claude Code?

Claude Code is Anthropic's official CLI tool for interacting with Claude AI. It can be configured to use OpenCode's free API endpoint instead of Anthropic's direct API.

**Product Page**: https://claude.com/product/claude-code

---

## Available Free Models

> Auto-updated every 6 hours via GitHub Actions · Last updated: <!-- LAST_UPDATED --> `2026-07-12 07:41 IST`

<!-- FREE_MODELS_START -->
| Model ID | Status |
|----------|--------|
| `deepseek-v4-flash-free` | FREE |
| `mimo-v2.5-free` | FREE |
| `hy3-free` | FREE |
| `nemotron-3-ultra-free` | FREE |
| `north-mini-code-free` | FREE |
<!-- FREE_MODELS_END -->

---

## Prerequisites

| Requirement | Windows | Mac | Linux |
|-------------|---------|-----|-------|
| Node.js 18+ | [nodejs.org](https://nodejs.org/en/download) | [nodejs.org](https://nodejs.org/en/download) or `brew install node` | [nodejs.org](https://nodejs.org/en/download) or package manager |
| Package Manager | Chocolatey (`choco install nodejs`) | Homebrew (`brew install node`) | apt, yum, dnf, or pacman |

---

## Windows Installation

### 1. Install Node.js

**Option A - Chocolatey (Recommended):**
```powershell
choco install nodejs
```

**Option B - Direct Download:**
Download from https://nodejs.org/en/download and run the installer.

### 2. Install Claude Code

```powershell
npm install -g @anthropic-ai/claude-code
```

### 3. Configure Settings

Edit `%USERPROFILE%\.claude\settings.json`:

```powershell
code $env:USERPROFILE\.claude\settings.json
```

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://opencode.ai/zen",
    "ANTHROPIC_MODEL": "minimax-m2.5-free",
    "ANTHROPIC_API_KEY": "opencode-api-key",
    "ENABLE_TOOL_SEARCH": "true"
  }
}
```

---

## Mac Installation

### 1. Install Node.js

**Option A - Homebrew (Recommended):**
```bash
brew install node
```

**Option B - Direct Download:**
Download from https://nodejs.org/en/download and run the installer.

### 2. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 3. Configure Settings

Edit `~/.claude/settings.json`:

```bash
code ~/.claude/settings.json
```

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://opencode.ai/zen",
    "ANTHROPIC_MODEL": "minimax-m2.5-free",
    "ANTHROPIC_API_KEY": "opencode-api-key",
    "ENABLE_TOOL_SEARCH": "true"
  }
}
```

---

## Linux Installation

### 1. Install Node.js

**Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install nodejs npm
```

**Fedora/RHEL:**
```bash
sudo dnf install nodejs npm
```

**Arch:**
```bash
sudo pacman -S nodejs npm
```

### 2. Install Claude Code

```bash
sudo npm install -g @anthropic-ai/claude-code
```

### 3. Configure Settings

Edit `~/.claude/settings.json`:

```bash
code ~/.claude/settings.json
```

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://opencode.ai/zen",
    "ANTHROPIC_MODEL": "minimax-m2.5-free",
    "ANTHROPIC_API_KEY": "opencode-api-key",
    "ENABLE_TOOL_SEARCH": "true"
  }
}
```

---

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `ANTHROPIC_BASE_URL` | `https://opencode.ai/zen` | OpenCode API endpoint |
| `ANTHROPIC_MODEL` | `minimax-m2.5-free` | Model to use (pick any FREE model above) |
| `ANTHROPIC_API_KEY` | `opencode-api-key` | Your OpenCode API key |
| `ENABLE_TOOL_SEARCH` | `true` | Enable tool search feature |

## Quick Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive session |
| `claude -p "<prompt>"` | Run single prompt |
| `claude --verbose` | Enable verbose logging |

## Troubleshooting

- **Node not found**: Restart terminal after installation or add Node.js to PATH
- **Permission denied**: Use `sudo` on Linux/Mac or run as administrator on Windows
- **API errors**: Verify your `ANTHROPIC_BASE_URL` is correctly set to `https://opencode.ai/zen`

## Resources

- OpenCode Website: https://opencode.ai/
- Claude Code: https://claude.com/product/claude-code
- Node.js Downloads: https://nodejs.org/en/download
# Claude Code Free Setup Cheat Sheet

Quick reference for setting up Claude Code with OpenCode's free API endpoint.

## What is OpenCode?

OpenCode is an AI-powered coding assistant CLI tool that helps with software engineering tasks. It uses various LLM providers including Anthropic Claude.

**Website**: https://opencode.ai/

## What is Claude Code?

Claude Code is Anthropic's official CLI tool for interacting with Claude AI. It can be configured to use OpenCode's free API endpoint instead of Anthropic's direct API.

**Product Page**: https://claude.com/product/claude-code

---

## Available Free Models

> Auto-updated every 6 hours via GitHub Actions · Last updated: <!-- LAST_UPDATED --> `2026-07-12 07:41 IST`

<!-- FREE_MODELS_START -->
| Model ID | Status |
|----------|--------|
| `deepseek-v4-flash-free` | FREE |
| `mimo-v2.5-free` | FREE |
| `hy3-free` | FREE |
| `nemotron-3-ultra-free` | FREE |
| `north-mini-code-free` | FREE |
<!-- FREE_MODELS_END -->

---

## Prerequisites

| Requirement | Windows | Mac | Linux |
|-------------|---------|-----|-------|
| Node.js 18+ | [nodejs.org](https://nodejs.org/en/download) | [nodejs.org](https://nodejs.org/en/download) or `brew install node` | [nodejs.org](https://nodejs.org/en/download) or package manager |
| Package Manager | Chocolatey (`choco install nodejs`) | Homebrew (`brew install node`) | apt, yum, dnf, or pacman |

---

## Windows Installation

### 1. Install Node.js

**Option A - Chocolatey (Recommended):**
```powershell
choco install nodejs
```

**Option B - Direct Download:**
Download from https://nodejs.org/en/download and run the installer.

### 2. Install Claude Code

```powershell
npm install -g @anthropic-ai/claude-code
```

### 3. Configure Settings

Edit `%USERPROFILE%\.claude\settings.json`:

```powershell
code $env:USERPROFILE\.claude\settings.json
```

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://opencode.ai/zen",
    "ANTHROPIC_MODEL": "minimax-m2.5-free",
    "ANTHROPIC_API_KEY": "opencode-api-key",
    "ENABLE_TOOL_SEARCH": "true"
  }
}
```

---

## Mac Installation

### 1. Install Node.js

**Option A - Homebrew (Recommended):**
```bash
brew install node
```

**Option B - Direct Download:**
Download from https://nodejs.org/en/download and run the installer.

### 2. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 3. Configure Settings

Edit `~/.claude/settings.json`:

```bash
code ~/.claude/settings.json
```

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://opencode.ai/zen",
    "ANTHROPIC_MODEL": "minimax-m2.5-free",
    "ANTHROPIC_API_KEY": "opencode-api-key",
    "ENABLE_TOOL_SEARCH": "true"
  }
}
```

---

## Linux Installation

### 1. Install Node.js

**Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install nodejs npm
```

**Fedora/RHEL:**
```bash
sudo dnf install nodejs npm
```

**Arch:**
```bash
sudo pacman -S nodejs npm
```

### 2. Install Claude Code

```bash
sudo npm install -g @anthropic-ai/claude-code
```

### 3. Configure Settings

Edit `~/.claude/settings.json`:

```bash
code ~/.claude/settings.json
```

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://opencode.ai/zen",
    "ANTHROPIC_MODEL": "minimax-m2.5-free",
    "ANTHROPIC_API_KEY": "opencode-api-key",
    "ENABLE_TOOL_SEARCH": "true"
  }
}
```

---

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `ANTHROPIC_BASE_URL` | `https://opencode.ai/zen` | OpenCode API endpoint |
| `ANTHROPIC_MODEL` | `minimax-m2.5-free` | Model to use (pick any FREE model above) |
| `ANTHROPIC_API_KEY` | `opencode-api-key` | Your OpenCode API key |
| `ENABLE_TOOL_SEARCH` | `true` | Enable tool search feature |

## Quick Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive session |
| `claude -p "<prompt>"` | Run single prompt |
| `claude --verbose` | Enable verbose logging |

## Troubleshooting

- **Node not found**: Restart terminal after installation or add Node.js to PATH
- **Permission denied**: Use `sudo` on Linux/Mac or run as administrator on Windows
- **API errors**: Verify your `ANTHROPIC_BASE_URL` is correctly set to `https://opencode.ai/zen`

## Resources

- OpenCode Website: https://opencode.ai/
- Claude Code: https://claude.com/product/claude-code
- Node.js Downloads: https://nodejs.org/en/download
