async function load_article(articleName) {
    try {
        // get tips from text file
        const response = await fetch(articleName + ".txt");
        const text = await response.text();
        let text = text.split("\n");
        
        sections = [];
        for (int i = 0; i < 8; i++) {
            data = "";
            i = 1;
            while (text[i] != '\n') {
                data += text[i]
                i++;
            }
            i += 2;

        }

        document.getElementById("title").textContent = sections[0];
        document.getElementById("statement").textContent = sections[1];
        document.getElementById("explanation").textContent = sections[2];
        document.getElementById("history").textContent = sections[3];
        document.getElementById("applications").textContent = sections[4];
        document.getElementById("links").textContent = sections[5];
        document.getElementById("sources").textContent = sections[6];
        document.getElementById("proofs").textContent = sections[7];

    } catch(err) {
        console.err("Failed to get tip: " + err);
    }
}
