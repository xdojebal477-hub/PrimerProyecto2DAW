async function resumir() {
            const textArea = document.getElementById('inputText');
            const btn = document.getElementById('btnSummarize');
            const btnText = document.getElementById('btnText');
            const resultGroup = document.getElementById('resultGroup');
            const summaryText = document.getElementById('summaryText');

            //que no este vacio
            if (!textArea.value.trim()) {
                alert("Por favor, introduce algún texto.");
                return;
            }

            // estado de carga (ux)
            btn.disabled = true;
            btnText.innerHTML = 'PROCESANDO... <span class="loading">_</span>';
            resultGroup.style.display = 'none';

            try {
                
                const response = await fetch('/api/summarize', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: textArea.value })
                });

                if (!response.ok) throw new Error("Error en el servidor");

                const data = await response.json();

                summaryText.innerText = data.summary;
                resultGroup.style.display = 'block';
                
            } catch (error) {
                alert("Hubo un fallo al conectar con el servidor de IA.");
                console.error(error);
            } finally {
                
                btn.disabled = false;
                btnText.innerText = 'GENERAR RESUMEN';
            }
        }