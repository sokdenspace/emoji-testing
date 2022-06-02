// Fetch components app to reusable, cycle in another page
fetch('components/home/home.html')
.then(res => res.text())
.then(text => {
	let oldelem = document.querySelector("script#app-home");
	let newelem = document.createElement("div")
	newelem.innerHTML = text;
	oldelem.parentNode.replaceChild(newelem,oldelem);
});
