/**
 * Interactive features of index.html are implemented here
 */

function updateRequestMemAmount(ev) {

	// $('#coreNum')
	// $('#memSize')
	// $('#memUnit')
	// $('#totalMemRes')

	//totalMemRes = num processors * mem per core

	var coreNum = $('#coreNum').val();
	var memSize = $('#memSize').val();
	var memUnit = $('#memUnit').val();

	res = memSize * coreNum + memUnit;
	$('#totalMemRes').html("Total requested memory is " + res + ".");
}

$('#coreNum, #memSize, #memUnit').change(updateRequestMemAmount);
$(document.body).ready(updateRequestMemAmount);


function toggleLimit(ev) {


	//$(ev.target).next('.limit')

	/*.each(index, function (index, element) {
		$(element).prop("disabled", !$(ev.target).val());
	});*/
}

$('.toggleLimit').change(toggleLimit);