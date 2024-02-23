# Terminal Commands

Here are some useful terminal commands:

## PATH exports

```bash
export PATH=$PATH:/opt/homebrew/opt/djvulibre/bin
export PATH=$PATH:/Users/rajeshkumar/Library/Python/3.11/bin:/usr/bin/python3
export PATH="$PATH:$(ruby -e 'puts Gem.user_dir')/bin"
```
## Alias
```bash
alias qu='/Users/rajeshkumar/XXX/SAVE/CODE/multi-browser.sh'
alias qut='/Users/rajeshkumar/XXX/SAVE/CODE/physics-terms.sh'
alias bkp='open /Users/rajeshkumar/XXX/SAVE/CODE/Physics-Stewart.pdf'
alias bkl='open /Users/rajeshkumar/XXX/SAVE/CODE/LAlgebra-RonLarson.pdf'
alias dct='open /Users/rajeshkumar/XXX/SAVE/CODE/Phy-Dictionary.pdf'
alias o='open .'
alias opd='open https://drive.google.com/drive/..'
alias gadd='python3 tracker.py;cat fadd|xargs git add'
alias gct='git commit -m'
alias gsl='git stash list --date=local'
alias gdiff='git diff --color=always HEAD~1 HEAD | less -R'
alias gpush='git push -u origin main'
alias viz='vi ~/.zshrc'
alias src='source ~/.zshrc'
alias pl='mkdir -p gar;pdflatex -output-directory=gar'
alias gv='git remote add origin https://github.com/rajeshphy/<repo-1>.git'
alias gp='git remote add origin https://github.com/rajeshphy/<repo-1>.git'

```
## Function
```bash
function cdd(){cd /Users/rajeshkumar/XXX/X}
function cdg(){cd /Users/rajeshkumar/XXX/GIT}
function cdgp(){cd /Users/rajeshkumar/XXX/GITP}
function lf(){cat /Users/rajeshkumar/XXX/Nts/lf.tex}
function llf(){cat /Users/rajeshkumar/XXX/Nts/llf.tex}
function nest(){cat /Users/rajeshkumar/XXX/Nts/nested-button.py}
function vin(){open /Users/rajeshkumar/XXX/Nts/"$1".tex}
function vip(){open /Users/rajeshkumar/XXX/Nts/gar/"$1".pdf}
function vipp(){pdflatex -output-directory=/Users/rajeshkumar/XXX/Nts/gar /Users/rajeshkumar/XXX/Nts/"$1".tex;open /Users/rajeshkumar/XXX/Nts/gar/"$1".pdf}
function plo(){pdflatex -output-directory=gar "$1".tex;bibtex "gar/$1".aux;pdflatex -output-directory=gar "$1".tex;pdflatex -output-directory=gar "$1".tex;open "gar/$1".pdf}
function op() {open "gar/$1".pdf}

