function moveNo() {
    const noBtn = document.getElementById("noBtn");

    const x = Math.random() * 300;
    const y = Math.random() * 300;

    noBtn.style.position = "absolute";
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";

    const texts = ["Are you sure? 😏", "Think again 😜", "Galat choice 😈", "YES hi option hai 😂"];
    noBtn.innerText = texts[Math.floor(Math.random() * texts.length)];
}

function yesClicked() {
    alert("Yayyy!! I knew it 😍💖");
    window.location.href = "/chocolate";
}
