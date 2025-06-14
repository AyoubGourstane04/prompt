## Exercice 2.3 :

### 1- Prompt :
> "Creer une mini-application Web en HTML/CSS/JS qui simule une calculatrice simple."

**Resultat :**

*   HTML : `index1.html`
    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculatrice</title>
        <link rel="stylesheet" href="style1.css">
    </head>
    <body>
        <div class="calculator">
            <input type="text" id="display" disabled>
            <div class="buttons">
                <button onclick="clearDisplay()">C</button>
                <button onclick="appendCharacter('7')">7</button>
                <button onclick="appendCharacter('8')">8</button>
                <button onclick="appendCharacter('9')">9</button>
                <button onclick="appendCharacter('/')">÷</button>
                <button onclick="appendCharacter('4')">4</button>
                <button onclick="appendCharacter('5')">5</button>
                <button onclick="appendCharacter('6')">6</button>
                <button onclick="appendCharacter('*')">×</button>
                <button onclick="appendCharacter('1')">1</button>
                <button onclick="appendCharacter('2')">2</button>
                <button onclick="appendCharacter('3')">3</button>
                <button onclick="appendCharacter('-')">−</button>
                <button onclick="appendCharacter('0')">0</button>
                <button onclick="appendCharacter('.')">.</button>
                <button onclick="calculate()">=</button>
                <button onclick="appendCharacter('+')">+</button>
            </div>
        </div>
        <script src="script1.js"></script>
    </body>
    </html>
    ```

*   CSS : `style1.css`
    ```css
    body {
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f4f4f4;
    }

    .calculator {
        background-color: #fff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    #display {
        width: 100%;
        padding: 10px;
        font-size: 1.5em;
        text-align: right;
        border: none;
        margin-bottom: 10px;
    }

    .buttons button {
        width: 50px;
        height: 50px;
        margin: 5px;
        font-size: 1.2em;
        cursor: pointer;
    }
    ```

*   JS : `script1.js`
    ```javascript
    function appendCharacter(character) {
        document.getElementById("display").value += character;
    }

    function clearDisplay() {
        document.getElementById("display").value = "";
    }

    function calculate() {
        try {
            document.getElementById("display").value = eval(document.getElementById("display").value);
        } catch {
            document.getElementById("display").value = "Erreur";
        }
    }
    ```

**Observations :**

L'application générée est fonctionnelle mais présente une interface très minimaliste. L’absence de styles visuels spécifiques ne permet pas de reconnaître facilement qu’il s’agit d’une calculatrice, ce qui la rend moins claire et facile à utiliser.

### 2- Prompt :
> "Créer une mini-application Web en HTML/CSS/JS qui simule une calculatrice simple, avec un style comportant des boutons arrondis et des couleurs différentes. Les opérations (symboles) doivent être séparées des chiffres par des couleurs distinctes. Le fond de la calculatrice doit être légèrement sombre, et le champ qui simule l’écran doit être bien positionné par rapport aux boutons. L’affichage de la calculatrice doit être vertical. De plus, il faut gérer les erreurs telles que les erreurs de saisie, les erreurs de calcul, les erreurs d’interface (UI/UX), ainsi que les erreurs de logique et de syntaxe en JavaScript, afin d’obtenir une calculatrice bien présentée et fonctionnelle."

**Resultat :**

*   HTML : `index2.html`
    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculatrice</title>
        <link rel="stylesheet" href="style2.css">
    </head>
    <body>
        <div class="calculator">
            <input type="text" id="display" disabled>
            <div class="buttons">
                <div class="row">
                    <button class="operator" onclick="clearDisplay()">C</button>
                    <button class="operator" onclick="appendCharacter('/')">÷</button>
                    <button class="operator" onclick="appendCharacter('*')">×</button>
                    <button class="operator" onclick="deleteLast()">←</button>
                </div>
                <div class="row">
                    <button class="number" onclick="appendCharacter('7')">7</button>
                    <button class="number" onclick="appendCharacter('8')">8</button>
                    <button class="number" onclick="appendCharacter('9')">9</button>
                    <button class="operator" onclick="appendCharacter('-')">−</button>
                </div>
                <div class="row">
                    <button class="number" onclick="appendCharacter('4')">4</button>
                    <button class="number" onclick="appendCharacter('5')">5</button>
                    <button class="number" onclick="appendCharacter('6')">6</button>
                    <button class="operator" onclick="appendCharacter('+')">+</button>
                </div>
                <div class="row">
                    <button class="number" onclick="appendCharacter('1')">1</button>
                    <button class="number" onclick="appendCharacter('2')">2</button>
                    <button class="number" onclick="appendCharacter('3')">3</button>
                    <button class="equal" onclick="calculate()">=</button>
                </div>
                <div class="row">
                    <button class="number zero" onclick="appendCharacter('0')">0</button>
                    <button class="number" onclick="appendCharacter('.')">.</button>
                </div>
            </div>
        </div>
        <script src="script2.js"></script>
    </body>
    </html>
    ```

*   CSS : `style2.css`
    ```css
    body {
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #2e2e2e;
    }

    .calculator {
        background-color: #444;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        text-align: center;
        width: 250px;
    }

    #display {
        width: 100%;
        padding: 15px;
        font-size: 1.5em;
        text-align: right;
        border: none;
        background-color: #222;
        color: #fff;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    .buttons .row {
        display: flex;
        justify-content: space-between;
    }

    button {
        width: 50px;
        height: 50px;
        margin: 5px;
        font-size: 1.2em;
        cursor: pointer;
        border: none;
        border-radius: 10px;
        transition: 0.3s;
    }

    .number {
        background-color: #555;
        color: white;
    }

    .operator {
        background-color: #ff9800;
        color: white;
    }

    .equal {
        background-color: #4caf50;
        color: white;
    }

    button:hover {
        opacity: 0.8;
    }

    .zero {
        width: 110px;
    }
    ```

*   JS : `script2.js`
    ```javascript
    function appendCharacter(character) {
        const display = document.getElementById("display");
        if (display.value === "Erreur") display.value = "";
        display.value += character;
    }

    function clearDisplay() {
        document.getElementById("display").value = "";
    }

    function deleteLast() {
        const display = document.getElementById("display");
        display.value = display.value.slice(0, -1);
    }

    function calculate() {
        const display = document.getElementById("display");
        try {
            let result = eval(display.value);
            if (!isFinite(result)) throw new Error("Division par zéro impossible");
            display.value = result;
        } catch {
            display.value = "Erreur";
        }
    }
    ```

### 3- L’évaluation des différences entre les deux versions met en évidence plusieurs améliorations essentielles :

*   **Amélioration du design** : La seconde version offre une interface plus agréable avec des boutons arrondis et une distinction visuelle claire entre les chiffres et les opérateurs grâce à des couleurs adaptées. De plus, le fond plus sombre améliore le contraste et la lisibilité, tandis que la disposition verticale optimise l’ergonomie.

*   **Gestion avancée des erreurs** : Contrairement à la première version, la seconde intègre un bouton "←" pour corriger les erreurs de saisie et détecte les erreurs de calcul telles que la division par zéro. En cas de problème, l’affichage affiche "Erreur", garantissant une interface plus intuitive et robuste.

*   **Expérience utilisateur optimisée** : La séparation visuelle entre les chiffres et les opérateurs facilite la lisibilité et la compréhension des opérations. L’ajout d’un bouton zéro plus large améliore la saisie, tandis que les transitions fluides offrent une meilleure sensation d’interaction.