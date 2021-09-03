let input = document.querySelector("textarea");
        document.getElementById("upper-case").addEventListener("click", function(){
            input.value = input.value.toUpperCase();
        });
        document.getElementById("lower-case").addEventListener("click", function(){
            input.value = input.value.toLowerCase();
        });
        document.getElementById("proper-case").addEventListener("click", function(){
            input.value = input.value.split(' ').map(w => w[0].toUpperCase() + w.substr(1).toLowerCase()).join(' ');
        });
        document.getElementById("sentence-case").addEventListener("click", function(){
            input.value = input.value.toLowerCase().replace(/(^\s*\w|[\.\!\?]\s*\w)/g,function(c){return c.toUpperCase()});
        });
        function download(){
            let text = document.querySelector("textarea").value;
            text = text.replace(/\n/g, "\r\n"); // To retain the Line breaks.
            let blob = new Blob([text], { type: "text/plain"});
            let anchor = document.createElement("a");
            anchor.download = "text.txt";
            anchor.href = window.URL.createObjectURL(blob);
            anchor.target ="_blank";
            anchor.style.display = "none";
            document.body.appendChild(anchor);
            anchor.click();
            document.body.removeChild(anchor);}