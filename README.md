# browser_from_terminal

# Browser From Terminal

A simple Python automation project that lets you search Google directly from your terminal using a custom alias command.

Instead of opening a browser manually and typing your search query, you can simply run:

```bash
google python decorators
```

and Safari automatically opens a filtered Google search.

---

# Technologies Used

* Python
* Terminal / Zsh
* VSCode
* Python `webbrowser` module

---

# Features

* Search Google directly from terminal
* Opens results automatically in Safari
* Custom terminal alias support
* Website filtering support
* Searches only selected websites:

  * Reddit
  * StackOverflow
  * Medium

---

# How It Works

The project uses:

* Python to process terminal input
* `sys.argv` to read search queries
* `webbrowser` module to open Safari automatically
* A terminal alias to make the command easy to use

Example:

```bash
google python list comprehension
```

This gets converted into a Google search URL and opens in Safari.

---

# What I Learned

Through this project, I learned:

* How terminal aliases work
* How to edit the `.zshrc` configuration file
* How Python receives terminal arguments using `sys.argv`
* How to use Python’s `webbrowser` module
* How URLs and search queries are generated dynamically
* Basic automation using Python and terminal commands

---

# Project Structure

```text
browser-from-terminal/
│
├── main.py
└── README.md
```

---

# Setup Instructions

## 1. Clone the repository

```bash
git clone <your-repo-link>
```

---

## 2. Navigate into the folder

```bash
cd browser-from-terminal
```

---

## 3. Add terminal alias

Open `.zshrc`:

```bash
nano ~/.zshrc
```

Add this line:

```bash
alias google='python3 /FULL/PATH/TO/main.py'
```

Example:

```bash
alias google='python3 ~/browser-from-terminal/main.py'
```

Save and exit.

---

## 4. Reload terminal configuration

```bash
source ~/.zshrc
```

---

# Running the Project

Now simply run:

```bash
google machine learning roadmap
```

Safari will automatically open a Google search filtered to supported websites.

---

# Example Search Filter

The project automatically searches within:

```text
(site:reddit.com OR site:stackoverflow.com OR site:medium.com)
```

This helps get more useful technical results.

---

# Demo



https://github.com/user-attachments/assets/a401ddae-4972-49c2-b882-f7fb5af92eb6



---

# Future Improvements

* Support for Chrome and Firefox
* AI-powered search suggestions
* More website filters
* Better CLI formatting
* Custom search presets
* Voice commands

---








