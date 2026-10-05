# Church Translate Skill for Claude Code

A [Claude Code](https://claude.com/claude-code) skill that translates between **French and English** using the vocabulary, grammar, and style of The Church of Jesus Christ of Latter-day Saints: the scriptures, general conference, manuals, and the *Liahona*.

The goal is a translation that reads as if it came from churchofjesuschrist.org in the target language, not a word-for-word rendering.

## What it does

- **Uses official Church terms.** It works from a glossary of about 200 core terms, such as *ward → paroisse*, *stake → pieu*, *Relief Society → Société de Secours* and *sacrament meeting → réunion de Sainte-Cène*. If you install an official word list (see below), that list takes priority.
- **Quotes scripture instead of translating it.** Verses are inserted from the official text of the target language (King James Version / Segond 1880, Book of Mormon, Doctrine and Covenants, Pearl of Great Price). References are converted too: `D&C 4:2` → `D&A 4:2`, `1 Nephi 3:7` → `1 Néphi 3:7`. When it isn't sure of the exact wording, it looks it up on churchofjesuschrist.org or marks the passage for you to check.
- **Handles names and titles.** It uses the full name of the Church, avoids "Mormon Church" and "LDS", and follows each language's conventions for titles (*le président Nelson*, *Elder Bednar*, *frère*, *sœur*).
- **Uses the right prayer language.** "Thee/Thou" in English, *tu/te* when addressing God in French (as in the sacrament prayers), and *vous* when addressing the congregation.
- **Follows typography rules.** French non-breaking spaces and « guillemets »; American spelling in English.
- **Translates documents.** `.docx`, `.pptx`, `.xlsx` and `.pdf` files keep their layout. The result is saved next to the original (`name_FR.pptx`, `name_EN.docx`), and the original is never overwritten.
- **Flags uncertainties.** A short *Notes* section after the translation lists terms or quotations it couldn't confirm.

## Installation

The skill can be installed globally, so it works in every project, or in a single project.

**Global (recommended):**

```bash
git clone https://github.com/BolondaJM/church-translate-skill.git
```

```bash
cp -r church-translate-skill/skills/translate ~/.claude/skills/
```

On Windows PowerShell:

```powershell
Copy-Item -Recurse church-translate-skill\skills\translate $HOME\.claude\skills\
```

**For one project only:** copy `skills/translate` into `<your-project>/.claude/skills/`.

Restart Claude Code (or start a new session). If the install worked, `translate` appears in the list of available skills.

## Usage

Type `/translate to French` or `/translate to English`, followed by the text or a file path:

```
/translate to French Brothers and sisters, I bear my testimony that Jesus Christ lives.
```

> Mes frères et sœurs, je rends témoignage que Jésus-Christ est vivant.

```
/translate to English IFR_Righteous_Use_of_Technology_1_FR.pptx
```

> Creates `IFR_Righteous_Use_of_Technology_1_EN.pptx` with the same slides and layout.

Claude also uses the skill automatically when you ask for a translation of Church-related material without the slash command.

Other target languages (`/translate to Spanish`, …) follow the same method, but the bundled glossary only covers French and English, so those terms are checked against churchofjesuschrist.org.

## Adding an official word list (optional)

The skill can search a much larger terminology list, such as the Church translation department's English → French word list. That list is **not included** in this repository because it is not a public document. If you have access to one in `.rtf` format, convert it with:

```bash
pip install striprtf
```

```bash
python tools/convert_wordlist.py French_140_wordlist1.rtf ~/.claude/skills/translate/wordlist-140.md
```

The file must be named `wordlist-<something>.md` and placed in the skill folder. Each line has the form `English | French | Note`.

- When an entry has **no French translation**, the same word is used in both languages, and the converter marks it `(same word in French)`.
- If a term appears in both the word list and the glossary, the word list wins.
- Some source files merge two English terms into one entry (lines starting with `See:`). Review those by hand after converting.

`wordlist-*.md` files are git-ignored so they are never pushed by accident.

## Customizing

- **Add or correct terms:** edit `skills/translate/glossary.md`. It's a set of plain Markdown tables.
- **Change style rules:** edit `skills/translate/SKILL.md`, which contains the rules Claude follows.
- If Claude confirms a new term during a translation, it will offer to add it to the glossary.

Pull requests with corrections to the glossary are welcome. Please cite the official churchofjesuschrist.org page that uses the term.

## Repository layout

```
skills/translate/
  SKILL.md       Rules Claude follows for every translation
  glossary.md    Core English ⇄ French Church terms (~200 entries)
tools/
  convert_wordlist.py   Converts an .rtf word list into wordlist-*.md
```

## Disclaimer

This is an independent project and is not affiliated with or endorsed by The Church of Jesus Christ of Latter-day Saints. Official translations on [churchofjesuschrist.org](https://www.churchofjesuschrist.org) always take precedence. Review translations before publishing them.

## License

[MIT](LICENSE) © 2026 Jonathan Bolonda
