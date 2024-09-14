// sort
const sort = document.querySelector("[sort]")
if(sort){
    let url = new URL(window.location.href);
    const sortSelect = sort.querySelector("[sort-select");
    const sortClear = sort.querySelector("[sort-clear]")

    sortSelect.addEventListener("change",() => {
        const [sortKey, sortValue] = sortSelect.value.split("-");
        url.searchParams.set("sortKey", sortKey);
        url.searchParams.set("sortValue", sortValue);
        window.location.href = url.href;
    });

    sortClear.addEventListener("click", () => {
        url.searchParams.delete("sortKey");
        url.searchParams.delete("sortValue");
        window.location.href = url.href;
    });

    const sortKey = url.searchParams.get("sortKey");
    const sortValue = url.searchParams.get("sortValue");

    if(sortKey && sortValue){
        const string = `${sortKey}-${sortValue}`;
        const optionSelected = sortSelect.querySelector(`option[value="${string}"]`)
        optionSelected.selected = true;
    }
}
//End sort

//Delete
const buttonDelete = document.querySelectorAll("[button-delete]");
if(buttonDelete.length > 0){
    const formDeleteItem = document.querySelector("[form-delete-item]");
    const path = formDeleteItem.getAttribute("data-path");
    buttonDelete.forEach(button => {
        button.addEventListener("click", ()=>{
            const isConfirm = confirm("Bạn có chắc muốn huỷ đơn này?");
            if(isConfirm){
                const id = button.getAttribute("data-id");
                console.log(id);
                console.log(path)
                const action = `${path}/${id}?_method=DELETE`;
                formDeleteItem.action = action;
                formDeleteItem.submit();
            }
        });
    });
}
//End Delete