document.addEventListener("DOMContentLoaded", function () {
	const interviewModeCheckbox = document.querySelector("#interviewMode");
	const profileCards = document.querySelectorAll(".profile-card");

	function MOdoEntrvista() {
		return !!(interviewModeCheckbox && interviewModeCheckbox.checked);
	}

	for (const card of profileCards) {
		const img = card.querySelector("img");
		if (!img) continue;

		const bioText = img.getAttribute("data-bio") || "";

		const bioDiv = document.createElement("div");
		bioDiv.classList.add("bio-info");
		bioDiv.textContent = bioText;
		card.appendChild(bioDiv);

		img.addEventListener("mouseenter", function () {
			if (!MOdoEntrvista()) return;
			bioDiv.style.display = "flex";
		});

		img.addEventListener("mouseleave", function () {
			if (!MOdoEntrvista()) return;
			bioDiv.style.display = "none";
		});
	}

	if (interviewModeCheckbox) {
		interviewModeCheckbox.addEventListener("change", function () {
			if (MOdoEntrvista()) return;
			const bios = document.querySelectorAll(".profile-card .bio-info");
			for (const bio of bios) bio.style.display = "none";
		});
	}
});
