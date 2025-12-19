 # Copilot Instructions for Learning-Python Repository

## Project Overview
This is an educational Python learning repository focused on **Python 101 Pythonic** concepts. It contains structured exercises progressing from basic data types to control flow, organized by topic with both verbose and Pythonic approaches shown.

## Repository Structure

### Main Organization
- **`Python101_Pythonic/`** - Core learning modules
  - `01-Data-Type&Expression/` - Basic types, operators, expressions
  - `02-Basic-String&List/` - String and list manipulation, `map()`, `split()`
  - `03-Selection/` - Control flow with if/elif/else, practical scenarios
- **`file-debug.py`** - Standalone debug/scratch file for testing snippets
- **`README.md`** - Minimal documentation

### File Naming Conventions
- Exercise files: `ex{MODULE}_{TOPIC}[.variants].py` (e.g., `ex02_12_map&split.py`)
- Some files have variants appended (e.g., `ex02_10_0.py`, `ex02_10_1.py`)
- Module numbers: 01, 02, 03, etc.

## Code Patterns & Conventions

### Educational Structure
# Copilot Instructions — Learning-Python (EN / TH)

Purpose / วัตถุประสงค์
- English: Short guidance for AI coding agents working on this educational Python exercises repo.
- ไทย: แนวทางสั้นๆ สำหรับเอเย่นต์โค้ดที่ทำงานกับชุดแบบฝึกหัด Python ในโปรเจคนี้

Quick start / เริ่มใช้งานเร็ว
- Run a single exercise: `python Python101_Pythonic/01-Data-Type&Expression/ex01_01.py`
- เปิดไฟล์ตัวอย่าง: `Python101_Pythonic/03-Selection/03-1-Flowchart&if-else/ex03_if_elif_else_basic._01.py`

Layout / โครงสร้างโปรเจค
- `Python101_Pythonic/` — หลักสูตรแยกเป็นโมดูลตามหัวข้อ
  - `01-Data-Type&Expression/`, `02-Basic-String&List/`, `03-Selection/`
- `file-debug.py` — ไฟล์ scratch สำหรับทดลองสั้นๆ

Conventions & patterns (project-specific)
- Dual approach: each exercise usually shows a verbose/traditional solution (commented) and a Pythonic solution (executable).
  - Example: `ex01_01.py` contains a commented step-by-step block then a one-line `map(int, input().split())` solution.
- Language: comments and descriptions are written in Thai — keep variable names and comments consistent with Thai when adding exercises.
- Type hints: functions often use simple type hints (e.g., `def check_ping(status: int) -> str`). Keep them where appropriate.

Naming rules
- Exercise files: `ex{MODULE}_{TOPIC}[.variant].py` (e.g. `ex02_10_1.py`).

How to add a new exercise / วิธีเพิ่มแบบฝึกหัดใหม่
1. Create file under the appropriate module folder, name it `exXX_YY.py`.
2. Include a commented "traditional" section (triple quotes) that explains the steps in Thai.
3. Provide a Pythonic implementation below and a minimal `call_*()` demo or `if __name__ == '__main__':` test.
4. Use type hints for function signatures and f-strings for output where helpful.

Examples to inspect / ตัวอย่างไฟล์สำคัญ
- `Python101_Pythonic/01-Data-Type&Expression/ex01_01.py` — input parsing example.
- `Python101_Pythonic/02-Basic-String&List/ex02_01.py` — use of `range()` and list creation.
- `Python101_Pythonic/03-Selection/03-1-Flowchart&if-else/ex03_if_elif_else_basic._01.py` — multi-case examples and `call_*()` patterns.

Development notes / หมายเหตุการพัฒนา
- No external dependencies — standard library only. Use Python 3.8+.
- Run individual exercises directly with `python <path-to-file>`.

What the agent should do first / สิ่งที่เอเย่นต์ควรทำก่อน
- Read the target exercise file and follow the existing comment+solution structure.
- Preserve Thai-language comments and the educational "teach then show" pattern.

Edit policy / นโยบายการแก้ไข
- Keep changes focused and minimal — do not reformat unrelated files.
- When adding exercises, follow naming, commenting, and test patterns shown above.

Feedback / ข้อเสนอแนะ
- If you want this translated fully into Thai-only, or expanded with git/workflow rules, tell me which sections to expand.

Last updated: 2025-11-13
- `file-debug.py` serves as a scratch file for testing concepts
