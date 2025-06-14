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
