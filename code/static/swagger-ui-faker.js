window.addEventListener("load", () => {
  const targetOperationId = "registre";

  const injectButton = () => {
    const block = document.querySelector(`.opblock[id*="${targetOperationId}"]`);
    if (!block || block.offsetParent === null) return;

    const executeBtn = block.querySelector("button.execute");
    const cancelBtn = block.querySelector("button.cancel");
    let insertBtn = block.querySelector(".insert-fake-btn");

    // Si no hay botones visibles aún, no hacemos nada
    if (!executeBtn || !cancelBtn) return;

    // Si ya existe, solo mostrarlo de nuevo si estaba oculto
    if (insertBtn) {
      insertBtn.style.display = "inline-block";
      return;
    }

    // Crear el botón
    insertBtn = document.createElement("button");
    insertBtn.className = "btn insert-fake-btn";
    insertBtn.innerText = "🧪 Insert fake data";

    insertBtn.onclick = async () => {
      const response = await fetch("/api/auth/registre/example");
      const data = await response.json();
      const value = JSON.stringify(data, null, 2);
      const textarea = block.querySelector("textarea");

      if (!textarea) {
        alert("❌ No se encontró el textarea");
        return;
      }

      const setter = Object.getOwnPropertyDescriptor(
        window.HTMLTextAreaElement.prototype,
        "value"
      ).set;
      setter.call(textarea, value);

      textarea.dispatchEvent(new Event("input", { bubbles: true }));
      textarea.dispatchEvent(new Event("change", { bubbles: true }));
    };

    // Insertar antes del botón Execute
    executeBtn.parentNode.insertBefore(insertBtn, executeBtn);

    // Ocultar el botón al cancelar
    cancelBtn.addEventListener("click", () => {
      console.log("🛑 Cancel → ocultando botón");
      insertBtn.style.display = "none";
    });
  };

  const observer = new MutationObserver(() => injectButton());
  observer.observe(document.body, { childList: true, subtree: true });

  setTimeout(() => injectButton(), 1000);
});
