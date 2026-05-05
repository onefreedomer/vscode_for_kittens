## Настройка VS Code и kitty terminal для создания своих программ (kittens).
1. Скачайте репозиторий kitty terminal.
```bash
git clone https://github.com/kovidgoyal/kitty.git /путь/к/kitty_src
``` 
2. Создайте директорию, где будет хранится `ваш_kitten.py`. Для этого может подойти `~/.config/kitty`.
3. Создайте внутри директорию `.vscode` с файлом `settings.json`, содержащий
```json
{
    "python.analysis.extraPaths": [
        "/путь/к/kitty_src"
    ]
}
```
4. Добавьте в файл настроек `kitty.conf` клавишу, по которой будет активироваться Ваш kitten.
```cfg
map hot_key kitten ваш_kitten.py
```
5. Готово!<br>
Пример оформления таких настроек с kitten приведен в директории `kitty` данного репозитория.