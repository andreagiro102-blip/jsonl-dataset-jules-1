# Interrompe lo script in caso di errori nativi di PowerShell
$ErrorActionPreference = "Stop"

Write-Host "Inizio procedura di merge automatico di tutte le PR aperte su main..." -ForegroundColor Cyan

# 1. Assicurati che il repository locale sia pulito e aggiornato
git fetch origin
git checkout main
git pull origin main

# 2. Ottieni la lista degli ID delle PR aperte che puntano al main
# Utilizza GitHub CLI per estrarre solo i numeri delle PR in formato JSON
Write-Host "Recupero delle Pull Request aperte..."
$prList = gh pr list --base main --state open --json number --jq '.[].number'

if (-not $prList) {
    Write-Host "Nessuna Pull Request aperta trovata verso il branch main." -ForegroundColor Yellow
    exit
}

# Assicurati che $prList sia un array anche se c'è una sola PR
if ($prList -isnot [array]) {
    $prList = @($prList)
}

# 3. Itera su ogni Pull Request trovata
foreach ($pr in $prList) {
    Write-Host "--------------------------------------------------"
    Write-Host "Gestione della Pull Request #$pr..." -ForegroundColor Cyan
    
    # Esegui il checkout del branch della PR per scaricarlo localmente
    gh pr checkout $pr
    
    # Cattura il nome del branch corrente
    $prBranch = (git branch --show-current).Trim()
    
    # Torna sul branch main
    git checkout main
    
    # 4. Esegui il merge con la strategia 'union'
    Write-Host "Esecuzione del merge di '$prBranch' in main con risoluzione conflitti 'union'..."
    
    # Esegui il merge
    git merge $prBranch --no-ff --strategy-option=union -m "Merge automatico PR #$pr (strategia union)"
    
    # Controlla se il comando git precedente ha generato un errore
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Merge di #$pr completato con successo." -ForegroundColor Green
    } else {
        Write-Host "❌ Errore irreversibile durante il merge di #$pr che la strategia union non è riuscita a risolvere." -ForegroundColor Red
        Write-Host "Annullamento del merge in corso..." -ForegroundColor Yellow
        git merge --abort
        exit 1
    }
}

Write-Host "--------------------------------------------------"
Write-Host "Tutte le PR sono state unite localmente sul branch main." -ForegroundColor Green
Write-Host "Controlla accuratamente il codice per assicurarti che non ci siano errori dovuti alla strategia union." -ForegroundColor Yellow
Write-Host "Se tutto è corretto, puoi inviare le modifiche con:"
Write-Host "git push origin main" -ForegroundColor Cyan
