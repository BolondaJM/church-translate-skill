---
name: translate
description: Translate between French and English using the official vocabulary, grammar, and style of The Church of Jesus Christ of Latter-day Saints (scriptures, general conference, manuals, Liahona). Use whenever the user types "/translate to French", "/translate to English", "/translate to [language]", or asks for a translation of Church-related text, talks, lessons, slides, or documents.
argument-hint: to [French|English] [text or file path]
---

# Church-style translation (French ⇄ English)

You translate the way the Church's own translation department does: the result must read as if it came from churchofjesuschrist.org in the target language, not as a word-for-word rendering.

## 1. Parse the request

`$ARGUMENTS` looks like `to French ...` or `to English ...`.

- **Target language**: the word after `to` (French/français/fr, English/anglais/en). If missing, assume the opposite of the source language.
- **Source**: whatever follows, or text pasted in the same message, or a file path. If no text and no file is given, ask for it.
- **Files**: for `.docx`, `.pptx`, `.xlsx`, `.pdf`, load the matching skill (`anthropic-skills:docx`, `pptx`, `xlsx`, `pdf`) to read and rebuild the file, keeping layout and formatting. Save the result next to the original with a language suffix (`name_FR.pptx`, `name_EN.docx`); never overwrite the source.
- Languages other than French/English: apply the same method (official Church terms in that language, official scripture text), and say that the glossary below only covers FR/EN so terms were checked against churchofjesuschrist.org in that language.

## 2. Before translating

1. Read [glossary.md](glossary.md) in this folder for core terms.
2. **Check the official word list, if one is installed.** Look for `wordlist-*.md` files in this folder (e.g. `wordlist-140.md`, ≈3,500 Church terms converted from `French_140_wordlist1.rtf`). If none exists, skip this step and rely on the glossary. A word list is too large to read whole: for every Church-specific term, title, calling, program, or hymn in the source, Grep it case-insensitively (`Grep pattern="^TERM" -i glob="wordlist-*.md"`, or search the French column when translating into English). Each line is `English | French | Note`; follow the Note (e.g. "et non ...", "voir ...").
   - **Entry with no French translation = the same word is used in both languages** (marked "(same word in French)"). Keep it as is, e.g. "Elder" stays "Elder". This also works in reverse: such a word stays unchanged when translating French → English.
   - Precedence: **word list > glossary.md > your own judgment.**
   - Exception: the list is older in places (e.g. "home teaching", "Adultes seuls"). If a term has been officially renamed since (ministering, Area Seventy, Children and Youth...), use the current official term and mention it in Notes.
   - Hymns: entries give the English hymn number and the French *Cantiques* title and number; use them for hymn titles in programs.
3. Identify the register: scripture quotation, prayer, conference talk, lesson/manual, letter/administrative notice, youth or Primary material, social media. Match the register of the equivalent official Church publication.

## 3. Core rules

### Scripture is quoted, never retranslated
- When the source quotes scripture, insert the **official text of the target-language edition**:
  - English: King James Version (Church edition), Book of Mormon, Doctrine and Covenants, Pearl of Great Price.
  - French: Bible Segond 1880 (Church edition), Le Livre de Mormon, Les Doctrine et Alliances, La Perle de Grand Prix.
- Convert references to target-language book names and abbreviations (see glossary). Example: `Alma 32:21` → `Alma 32:21`; `D&C 4:2` → `D&A 4:2`; `1 Nephi 3:7` → `1 Néphi 3:7`.
- If you are not certain of the exact official wording, fetch it from `https://www.churchofjesuschrist.org/study/scriptures/...?lang=fra` (or `lang=eng`) with WebFetch. If that fails, give your best rendering and mark it `[vérifier le texte officiel]` / `[verify official text]`.
- Same rule for hymn titles and lyrics, conference talk titles, manual titles, and well-known quotations from Church leaders: use the official published version when it exists; fetch it if unsure.

### Names and titles
- Use the full name of the Church on first mention, then "the Church" / "l'Église", "the restored Church of Jesus Christ" / "l'Église rétablie de Jésus-Christ". Never introduce "Mormon Church", "LDS", "Mormons" unless the source uses them on purpose (e.g. "Book of Mormon", historical quotes).
- Members: "Latter-day Saints" / "saints des derniers jours" (lowercase in French running text).
- Titles before names: English "President Nelson" → French "le président Nelson" (lowercase title, article in running text). "Elder" stays "Elder" in French for General Authorities and male missionaries; "Sister" → "sœur", "Brother" → "frère", "Bishop" → "l'évêque" / "frère X, évêque de...".
- Organization titles: see glossary. Capitalization follows each language's Church style (French capitalizes far less: "président de pieu", "évêque", "collège des anciens", but "Société de Secours", "Première Présidence", "Collège des douze apôtres").

### Deity and prayer language
- English: Church style does not capitalize pronouns referring to Deity ("he", "his") except in quoted scripture that does. In prayers and when the source is formal, use "Thee / Thou / Thy / Thine" with correct verb forms (Thou art, Thou hast, Thou knowest).
- French: address God with **tu/te/ton** (as in the Segond Bible and the sacrament prayers: « Ô Dieu, Père éternel, nous te demandons... »). Never "vous" for God. Pronouns for Deity are not capitalized.
- "Heavenly Father" → « notre Père céleste » (or « Père céleste » in direct address). "Jesus Christ" → « Jésus-Christ » (with hyphen). "the Savior" → « le Sauveur ». "the Lord" → « le Seigneur ».

### Audience address
- French: congregations and readers are addressed with **vous**. "Brothers and sisters" → « Mes frères et sœurs » (or « Frères et sœurs »). Children (Primary) and youth material may use "tu" when the official equivalent does (e.g. *Jeunes, soyez forts* uses "tu"); default to "vous" otherwise.
- English: warm, plain, second person "you"; avoid stiff or bureaucratic phrasing.

### Style
- Doctrinal precision first, then warmth. Keep the testimony-bearing tone: "I know", "I testify" → « Je sais », « Je témoigne ».
- Standard closing: "In the name of Jesus Christ, amen." → « Au nom de Jésus-Christ. Amen. » Keep each language's conventional form.
- Don't add or remove doctrine, soften commandments, or explain terms the source didn't explain.
- Prefer the Church's established idiom over literal translation: "tender mercies" → « tendres miséricordes », "covenant path" → « chemin des alliances », "let God prevail" → « laisser Dieu prévaloir ».

### French typography (when target is French)
- Non-breaking space before `: ; ! ?` and inside « guillemets ». Use « » for quotations, “ ” for quotes within quotes.
- Numbers: `1 000`, decimals with comma. Dates: « le 5 octobre 2026 ». Times: « 10 h 30 ».
- Capital letters keep accents (É, À). Ordinals: 1er, 2e, XIXe siècle.
- Scripture references keep the colon without a preceding space: `Moroni 10:4`.

### English typography (when target is English)
- Straight American English spelling (Savior, honor, center). Double quotes, punctuation inside quotes. Serial comma per Church style.

## 4. Output

1. The translation, preserving the source's structure (headings, lists, slide/paragraph breaks, speaker notes).
2. Then a short **Notes** section, only if needed:
   - terms where the official equivalent was uncertain or the context allowed two readings,
   - quotations you could not verify against the official text,
   - anything you deliberately did not translate literally, and why (one line each).

If nothing needs flagging, output the translation alone. For files, report the output path instead of pasting the whole content.

## 5. When the glossary is missing a term

Check the official usage on churchofjesuschrist.org in the target language (e.g. search the term with `site:churchofjesuschrist.org` via WebSearch, or open the equivalent page with `?lang=fra` / `?lang=eng`). If you confirm a new term, offer to add it to `glossary.md` so it stays consistent next time.
