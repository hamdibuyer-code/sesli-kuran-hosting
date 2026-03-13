@echo off
setlocal enabledelayedexpansion

cd /d D:\sesli_kuran_hosting
git config --global gc.auto 0

REM Bir seferde kaç mp3 eklensin?
set BATCH=200
set COUNT=0

for %%F in (public\audio_data\Ghamadi\*.mp3) do (
    git add "%%F"
    set /a COUNT+=1

    if !COUNT! GEQ %BATCH% (
        echo Commit atiliyor...
        git commit -m "Add audio batch"
        git push
        set COUNT=0
    )
)

REM Kalan dosyalar
if !COUNT! GTR 0 (
    echo Son commit...
    git commit -m "Add audio batch"
    git push
)

echo Tum mp3 dosyalari gonderildi.
pause
