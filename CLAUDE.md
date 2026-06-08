# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此仓库中工作时提供指导。

## 项目概述

`starred` 是一个 Python CLI 工具,从用户的 GitHub stars 生成并维护 Awesome 风格的列表。源码位于 `starred/`:`starred.py`(Click CLI 入口)和 `githubgql.py`(GitHub GraphQL 客户端)。

## 环境

- 包管理器使用 **`uv`**(已从 poetry 迁移)。安装依赖:`uv sync --dev`。
- 运行或测试 CLI 需要 `GITHUB_TOKEN`(GitHub personal access token)。

## 命令

- Lint:`uv run ruff check starred`
- 格式化:`uv run ruff format starred`(仅检查不修改:`uv run ruff format --check starred`)
- 构建:`uv build`
- 运行 / 集成测试:`uv run starred --username <user> --token ${GITHUB_TOKEN} --sort`

## 代码风格

- 使用 **Ruff** 做 lint 与格式化,配置在 `pyproject.toml` 的 `[tool.ruff]`:行长 200、lint 规则 `E/W/F`、字符串用单引号(`quote-style = "single"`)。
- 提交前确保 `ruff check` 与 `ruff format --check` 均通过(CI 严格执行)。

## 测试

- 无单元测试。验证标准为上述集成测试:使用有效的 `GITHUB_TOKEN` 针对真实 GitHub API 运行(CI 即运行此命令)。

## 工作流

- 在 feature 分支上开发,向 `main` 提 PR。
- 提交信息遵循 Conventional Commits 规范。
