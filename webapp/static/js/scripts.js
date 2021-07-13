/*---------------------------------------------------------------------
    File Name: custom.js
---------------------------------------------------------------------*/

$(function () {

    "use strict";

    /* JQuery Library Search Menu
    -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

    $(document).ready(function () {
        // const searchButton = document.getElementById('lib-search-btn');
        const searchInput = document.getElementById('lib-search');
        const msgSection = document.getElementById('data-msg');
        const resultItem = document.getElementById('result-item');
        const bookSet = document.getElementsByName('book');
        const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        const sendSearchData = (book) => {
            $.ajax({
                type: 'POST',
                url: '',
                data: {
                    'csrfmiddlewaretoken': csrf,
                    'book': book,
                },
                success: (res) => {
                    // console.log(res.data)
                    const data = res.data
                    bookSet.forEach(elem => {
                        elem.setAttribute("hidden", true);
                    })
                    if (Array.isArray(data)) {
                        data.forEach(book => {
                            const b = document.getElementById(`book_${book.pk}`)
                            if(b){
                                b.removeAttribute("hidden");
                            }
                        })
                    } else {
                        if (searchInput.value.length > 0) {
                            msgSection.removeAttribute("hidden");
                            resultItem.innerText = `${data}`;
                        } else {
                            msgSection.setAttribute("hidden", true);
                            bookSet.forEach(elem => {
                                elem.removeAttribute("hidden");
                            })
                        }
                    }
                },
                error: (err) => {
                    console.log(err)
                }
            })
        }

        // searchButton.addEventListener('click', searchHandler());
        searchInput.addEventListener('keyup', searchHandler);

        function searchHandler(e) {
            console.log(e.target.value);
            sendSearchData(e.target.value)
        }
    });
});

