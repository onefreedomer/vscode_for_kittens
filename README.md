## Настройка VS Code для создания своих программ (kittens) для kitty terminal.
1. Скачайте репозиторий kitty terminal.
```bash
git clone https://github.com/kovidgoyal/kitty.git /путь/к/kitty_src
``` 
2. Создайте директорию, где будет хранится `.py` файл kitten. Для этого может подойти `~/.config/kitty/`.
3. Создайте внутри директорию `.vscode` с файлом `settings.json` с содержимым:
```json
{
    "python.analysis.extraPaths": [
        "/путь/к/kitty_src"
    ]
}
```