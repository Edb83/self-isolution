$(document).ready(function () {
    "use strict";

    // Materialize initialization
    $(".dropdown-trigger").dropdown({ constrainWidth: false, coverTrigger: false });
    $(".sidenav").sidenav({ edge: "right" });
    $("select").formSelect();
    $('input#activity_name, textarea#activity_summary, textarea#activity_details, textarea#activity_equipment, input#category_name, textarea#category_summary').characterCounter();
    $('.modal').modal();

    // Adds validation to Materialize select fields
    // Code Institute
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50",
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336",
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                display: "block",
                height: "0",
                padding: "0",
                width: "0",
                position: "absolute",
            });
        }
        $(".select-wrapper input.select-dropdown")
            .on("focusin", function () {
                $(this)
                    .parent(".select-wrapper")
                    .on("change", function () {
                        if (
                            $(this)
                                .children("ul")
                                .children("li.selected:not(.disabled)")
                                .on("click", function () { })
                        ) {
                            $(this).children("input").css(classValid);
                        }
                    });
            })
            .on("click", function () {
                if (
                    $(this)
                        .parent(".select-wrapper")
                        .children("ul")
                        .children("li.selected:not(.disabled)")
                        .css("background-color") === "rgba(0, 0, 0, 0.03)"
                ) {
                    $(this).parent(".select-wrapper").children("input").css(classValid);
                } else {
                    $(".select-wrapper input.select-dropdown").on(
                        "focusout",
                        function () {
                            if (
                                $(this)
                                    .parent(".select-wrapper")
                                    .children("select")
                                    .prop("required")
                            ) {
                                if (
                                    $(this).css("border-bottom") != "1px solid rgb(76, 175, 80)"
                                ) {
                                    $(this)
                                        .parent(".select-wrapper")
                                        .children("input")
                                        .css(classInvalid);
                                }
                            }
                        }
                    );
                }
            }
        );
    }
});

$(document).click(function () {
    "use strict";
    // Fixes bug with Materialize select elements not working with iOS
    // https://stackoverflow.com/a/52851046
    $('li[id^="select-options"]').on('touchend', function (e) {
        e.stopPropagation();
    });
});