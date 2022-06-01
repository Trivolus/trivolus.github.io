//
function newItem() {
    var item = document.getElementById("input").value;
    var ul = document.getElementById("list");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode ("-" + item));
    ul.appendChild(li);
    document.getElementById("input").value = "";
    li.onclick = removeItem;
}

//When enter key is pressed execute function newItem()
document.body.onkeyup = function(e) {
    if (e.keyCode == 13) {
        newItem();
    }
};
//delete item
function removeItem(e) {
    e.target.parentElement.removeChild(e.target);
}

//jQuery


/* <script>
$().ready(function(){
//TO-DO-LIST
    //add new item via enter key
    $('ul').on('keypress', function createItem(e) {

        if (e.which == 13){
            $('ul').append('<li"><input class="list-group-item"></div>');
            
        };
    })//add item via clicking button
        if ($('.button').on('click', function addItem(e){
            $('ul').append('<li"><input class="list-group-item"></div>');
    }));
});
     */