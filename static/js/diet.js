$(document).ready(function () {
    $(".query").submit("click", function (event) {
        event.preventDefault();
        $(".results").children().remove();
        $(".nutritional-container").children().remove();
        var userQuery = ($("input[name='tags']").val()).replace(/[\s-+(),.]/g, " ");
        searchApiWith(userQuery);
    });
});

// User key for API access
var ndbKey = "gA9qgMluHacPOMK4aLSaZP87vYT3Sobd5Sqt7bH6";


// Start a new search
function searchApiWith(userQuery) {

    var parameters = {
        format: 'json',
        q: userQuery,
        api_key: ndbKey
    };
    // Get food names and foodIds
    var result = $.ajax({
        url: "https://api.data.gov/usda/ndb/search/",
        data: parameters,
        type: "GET"
    }).done(function (result) {
        $(".nutritionList-container").children().remove()
        var searchResults = result.list.item,
            multiTagsArray = $.each(userQuery.split(/[\s]/), function (index, item) {
            });

//			console.log(result);

        reviewSearchResults(searchResults, multiTagsArray)

        // When a food item is selected a second API search is completed
        // to retreive its nutritional-container information using the items foodId

        $(".results li").on("click", function () {
            //var foodId = $(this).attr("data-id");
            $(this).clone(true).appendTo($(".queryresults ul"));
            var foodId = $(this).attr("data-id");
            getNutritionalInformation(foodId);
            //getNutritionalInformation(foodId);
        });


    })
        .fail(function (e, x, thrownError) {
            if (thrownError == "Not Found") {
                showError();
            }
        });
};


// If only 1 tag was input by the user
// then print results whose primary tag matches the user input tag
// E.g. A search for "potato" would not print "Snacks, potato chips..."
// Else produce results that are refined based on all user input tags
// E.g. A search for "raw potato" would print all results with "raw" and "potato" as part of its name
function reviewSearchResults(searchResults, multiTagsArray) {
    var domToBeSetUp = true,
        relevantResults = 0;
    if (multiTagsArray.length === 1) {
        var singleTag = multiTagsArray[0];
        printSearchResults(domToBeSetUp, relevantResults, searchResults, singleTag);
    } else {
        refineSearchResults(domToBeSetUp, relevantResults, searchResults, multiTagsArray);
    }
    ;
}

function printSearchResults(domToBeSetUp, relevantResults, searchResults, singleTag) {
    $.each(searchResults, function (index, searchValue) {
        checkCaseInArray(singleTag, searchValue);
        if (tagLower == 0 || tagUpper == 0) {
            checkForFoodList(domToBeSetUp);
            domToBeSetUp = false;
            printResult(searchValue);
            relevantResults++;
        }
        ;
    });
    checkRelevantResults(relevantResults);
}

function refineSearchResults(domToBeSetUp, relevantResults, searchResults, multiTagsArray) {
    $.each(searchResults, function (index, searchValue) {
        var thisResultRelevance = 0,
            resultNamesArray =
                $.each((searchValue.name)
                    .replace(/,/g, "")
                    .split(" "), function (index, item) {
                });

        // Counts how many user input tags are in each result
        $.each(multiTagsArray, function (index, tagValue) {
            checkCaseInArray(tagValue, searchValue);
            if (tagLower >= 0 || tagUpper >= 0) {
                thisResultRelevance++;
            }
            ;
        });

        // If the result is relevant based on all user input tags then it gets printed
        if (thisResultRelevance === multiTagsArray.length) {
            // Set up the DOM when first relevant result is found
            checkForFoodList(domToBeSetUp);
            domToBeSetUp = false;
            printResult(searchValue);
            relevantResults++;
        }
        ;
    });
    checkRelevantResults(relevantResults);
};

// Check if the DOM is ready to be populated with food items
function checkForFoodList(domToBeSetUp) {
    if (domToBeSetUp) {
        setUpDomToPrint();
    }
    ;
}

// If no relevant results were found present error
function checkRelevantResults(relevantResults) {
    if (relevantResults === 0) {
        showError();
    }
    ;
}


function getNutritionalInformation(foodId) {
    $(".nutritional-container").children().remove();
    var parameters = {
        format: 'json',
        ndbno: foodId,
        api_key: ndbKey
    };
    var result = $.ajax({
        url: "https://api.data.gov/usda/ndb/reports/",
        data: parameters,
        type: "GET"
    }).done(function (result) {
        createNutritionList(result);
        //$('.nutritional-container').append(nutritionalInformation);
//		console.log(result.report);
    });
}

var resultList = []
// Create a copy of the template nutrition list
// and append it under nutritional-container information
function createNutritionList(result) {
    // Create a temporary copy of the template
    var temp = $(".templates .nutrition").clone();
    var path = result.report.food;
    var nutrPath = path.nutrients;

    // Search to API object by index.name rather than index
    var lookup = {};
    for (var i = 0, len = nutrPath.length; i < len; i++) {
        // lookup[nutrPath[i].name.replace(/[\s-+(),.]/g, "")] = nutrPath[i];
        lookup[nutrPath[i].nutrient_id] = nutrPath[i];
    }
    resultList.push(lookup)
    // console.log(lookup)
    // Prints the wanted search results into the temporary DOM's elements
    // updateNutrListElement(".calories", lookup[208], temp);
    // updateNutrListElement(".fat", lookup[204], temp);
    // updateNutrListElement(".saturated", lookup[606], temp);
    // updateNutrListElement(".fiber", lookup[291], temp);
    //updateNutrListElement(".water", lookup[255], temp);
    // updateNutrListElement(".zinc", lookup[309], temp);
    // updateNutrListElement(".iron", lookup[303], temp);
    // updateNutrListElement(".folate", lookup[435], temp);
    // updateNutrListElement(".protein", lookup[203], temp);
    // updateNutrListElement(".sugars", lookup[269], temp);
    // updateNutrListElement(".calcium", lookup[301], temp);
    // updateNutrListElement(".phosphorus", lookup[305], temp);
    // updateNutrListElement(".vitamin_A", lookup[318], temp);
    // updateNutrListElement(".vitamin_B6", lookup[415], temp);
    // updateNutrListElement(".vitamin_B12", lookup[418], temp);
    // updateNutrListElement(".vitamin_C", lookup[401], temp);
    temp.find(".food").text(path.name);
    temp.find(".carbohydrate").text(
        (+lookup[205].value -
            +lookup[291].value).toFixed(1) +
        lookup[205].unit
    );

    return temp
//	Print all nutritional information in the console
//	$.each(nutrPath, function(index, nutrValue) {
//		console.log(nutrValue.name + ": " + nutrValue.value + nutrValue.unit);
//	});
}

var protein = 0
var sugars = 0
var calcium = 0
var phosphorus = 0
var vitamin_A = 0
var vitamin_B6 = 0
var vitamin_B12 = 0
var vitamin_C = 0


var rProtein = 56
var rCalcium = 1000
var rPhosphor = 1000
var rVitamin_A = 600
var rVitamin_B6 = 2
var rVitamin_B12 = 6
var rVitamin_C = 75
var rSugar = 30


$("#submit").click(function () {

    $(".queryresults li").each(function () {
        // var foodId = $(this).attr("data-id");
        // getNutritionalInformation(foodId);
        for (var i = 0; i < resultList.length; i++) {
            var validation = 0
            if (resultList[i][203] == null) {
                protein += validation
            } else {
                protein += parseFloat(resultList[i][203].value)
            }
            if (resultList[i][269] == null) {
                sugars += validation
            } else {
                sugars += parseFloat(resultList[i][269].value)
            }
            if (resultList[i][301] == null) {
                calcium += validation
            } else {
                calcium += parseFloat(resultList[i][301].value)
            }
            if (resultList[i][305] == null) {
                phosphorus += validation
            } else {
                phosphorus += parseFloat(resultList[i][305].value)
            }
            if (resultList[i][318] == null) {
                vitamin_A += validation
            } else {
                vitamin_A += parseFloat(resultList[i][318].value)
            }
            if (resultList[i][415] == null) {
                vitamin_B6 += validation
            } else {
                vitamin_B6 += parseFloat(resultList[i][415].value)
            }
            if (resultList[i][418] == null) {
                vitamin_B12 += validation
            } else {
                vitamin_B12 += parseFloat(resultList[i][418].value)
            }
            if (resultList[i][401] == null) {
                vitamin_C += validation
            } else {
                vitamin_C += parseFloat(resultList[i][401].value)
            }
        }
        resultList = []
    });

    if (sugars != 0) {
        var gprotein = (protein - rProtein) / rProtein * 100
        var gcalcium = (calcium - rCalcium) / rCalcium * 100
        var gsugars = (sugars - rSugar) / rSugar * 100
        var gphosphorus = (phosphorus - rPhosphor) / rPhosphor * 100
        var gvitamin_A = (vitamin_A - rVitamin_A) / rVitamin_A * 100
        var gvitamin_B6 = (vitamin_B6 - rVitamin_B6) / rVitamin_B6 * 100
        var gvitamin_B12 = (vitamin_B12 - rVitamin_B12) / rVitamin_B12 * 100
        var gvitamin_C = (vitamin_C - rVitamin_C) / rVitamin_C * 100

        $("#protein").text("Protein:  " + protein.toFixed(2) + " g")
        if (gprotein >= 0) {
            $("#gprotein").text(gprotein.toFixed(2) + "%")
            $("#gprotein").css({color: "green"})
        } else {
            $("#gprotein").text(gprotein.toFixed(2) + "%")
            $("#gprotein").css({color: "red"})
        }

        $("#sugars").text("Sugar:  " + sugars.toFixed(2) + " g")
        if (gsugars >= 0) {
            $("#gsugars").text(gsugars.toFixed(2) + "%")
            $("#gsugars").css({color: "green"})
        } else {
            $("#gsugars").text(gsugars.toFixed(2) + "%")
            $("#gsugars").css({color: "red"})
        }

        $("#calcium").text("Calcium:  " + calcium.toFixed(2) + " mg")
        if (gcalcium >= 0) {
            $("#gcalcium").text(gcalcium.toFixed(2) + "%")
            $("#gcalcium").css({color: "green"})
        } else {
            $("#gcalcium").text(gcalcium.toFixed(2) + "%")
            $("#gcalcium").css({color: "red"})
        }
        $("#phosphorus").text("Phosphorus:  " + phosphorus.toFixed(2) + " mg")
        if (gphosphorus >= 0) {
            $("#gphosphorus").text(gphosphorus.toFixed(2) + "%")
            $("#gphosphorus").css({color: "green"})
        } else {
            $("#gphosphorus").text(gphosphorus.toFixed(2) + "%")
            $("#gphosphorus").css({color: "red"})
        }

        $("#vitamin_A").text("Vitamin A:  " + vitamin_A.toFixed(2) + " ug")
        if (gvitamin_A >= 0) {
            $("#gvitamin_A").text(gvitamin_A.toFixed(2) + "%")
            $("#gvitamin_A").css({color: "green"})
        } else {
            $("#gvitamin_A").text(gvitamin_A.toFixed(2) + "%")
            $("#gvitamin_A").css({color: "red"})
        }

        $("#vitamin_B6").text("Vitamin B6:  " + vitamin_B6.toFixed(2) + " mg")
        if (gvitamin_B6 >= 0) {
            $("#gvitamin_B6").text(gvitamin_B6.toFixed(2) + "%")
            $("#gvitamin_B6").css({color: "green"})
        } else {
            $("#gvitamin_B6").text(gvitamin_B6.toFixed(2) + "%")
            $("#gvitamin_B6").css({color: "red"})
        }
        $("#vitamin_B12").text("Vitamin B12:  " + vitamin_B12.toFixed(2) + " ug")
        if (gvitamin_B12 >= 0) {
            $("#gvitamin_B12").text(gvitamin_B12.toFixed(2) + "%")
            $("#gvitamin_B12").css({color: "green"})
        } else {
            $("#gvitamin_B12").text(gvitamin_B12.toFixed(2) + "%")
            $("#gvitamin_B12").css({color: "red"})
        }
        $("#vitamin_C").text("Vitamin C:  " + vitamin_C.toFixed(2) + " mg")
        if (gvitamin_C >= 0) {
            $("#gvitamin_C").text(gvitamin_C.toFixed(2) + "%")
            $("#gvitamin_C").css({color: "green"})
        } else {
            $("#gvitamin_C").text(gvitamin_C.toFixed(2) + "%")
            $("#gvitamin_C").css({color: "red"})
        }
    }
    $("#information").css('display', 'block')
    protein = 0
    sugars = 0
    calcium = 0
    phosphorus = 0
    vitamin_A = 0
    vitamin_B6 = 0
    vitamin_B12 = 0
    vitamin_C = 0

});

$("#clear").click(function () {
    resultList = []
    $("#querylist").children().remove()
    $(".nInfo-name li").each(function () {
        $(this).text('')
    })
    $(".gInfo-name li").each(function () {
        $(this).text('')
    })
    $(".querylist-result").children().remove()
    $("#information").css('display', 'none');


})

// Create a new results list and provide secondary instruction
function setUpDomToPrint() {
    $(".results").append("<ul id='querylist' style='padding-top:10px; list-style-type: none;padding-inline-start: 10px;' class='food-list'></ul>");
    $(".nutritionList-container").append("<div class='instruction' style='padding-top: 15px;'><p>Click on a food item to display its nutritional information.</p></div>");
}

// Mitigate first letter capitalisation for user input tags
function checkCaseInArray(tag, value) {
    tagLower = value.name.indexOf(tag.charAt(0).toLowerCase() + tag.slice(1));
    tagUpper = value.name.indexOf(tag.charAt(0).toUpperCase() + tag.slice(1));
};

// Print food items found in first search along with their ndbno (data-id)
function printResult(searchValue) {
    $(".food-list").append("<li class='foodItem' data-id='" + searchValue.ndbno + "'>" + searchValue.name + "</li>");
};

// Place the nutritional value and unit inside the temporary element for the DOM
function updateNutrListElement(element, nutrient, temp) {
    var nutrLevel = +nutrient.value
    temp.find(element).text(nutrLevel.toFixed(1) + nutrient.unit);
};

// Provides error feedback if no results were found
function showError() {
    $(".results").append($('.templates .error').clone());
};

