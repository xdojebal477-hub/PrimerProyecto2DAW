document.addEventListener("DOMContentLoaded", function () {
	const interviewModeCheckbox = document.querySelector("#interviewMode");
	const profileCards = document.querySelectorAll(".profile-card");

	function MOdoEntrvista() {
        //devuelve true si el modo entrevista está activado o false si no lo está
		return !!(interviewModeCheckbox && interviewModeCheckbox.checked);
	}

	for (const card of profileCards) {   // Recorre todas las tarjetas de perfil
		const img = card.querySelector("img");// selecciona la imagen dentro de la tarjeta
		if (!img) continue;// si no hay imagen, pasa a la siguiente tarjeta

		const bioText = img.getAttribute("data-bio") || "";// obtiene el texto biográfico del atributo data-bio de la imagen

		const bioDiv = document.createElement("div");
		bioDiv.classList.add("bio-info");
		bioDiv.textContent = bioText;// establece el texto biográfico en el div
		card.appendChild(bioDiv);//lo metemos dentro de la tarjeta

		img.addEventListener("mouseenter", function () {
			if (!MOdoEntrvista()) return;// si no está en modo entrevista, no hace nada
			bioDiv.style.display = "flex";// muestra el div con la biografía
		});

		img.addEventListener("mouseleave", function () {
			if (!MOdoEntrvista()) return;
			bioDiv.style.display = "none";
		});
	}

	if (interviewModeCheckbox) {
		interviewModeCheckbox.addEventListener("change", function () {// cuando se cambia el estado del checkbox
			if (MOdoEntrvista()) return;// si está en modo entrevista, no hace nada
			const bios = document.querySelectorAll(".profile-card .bio-info");
			for (const bio of bios) bio.style.display = "none";// oculta todas las biografías
		});
	}
});
