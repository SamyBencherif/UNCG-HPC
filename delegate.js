/**
 * Interactive features of index.html are implemented here
 */

function updateRequestMemAmount(ev) {
	var coreNum = $('#coreNum').val();
	var memSize = $('#memSize').val();
	var memUnit = $('#memUnit').val();

	res = memSize * coreNum + memUnit;
	$('#totalMemRes').html("Total requested memory is " + res + ".");
}

$('#coreNum, #memSize, #memUnit').change(updateRequestMemAmount);
$(document.body).ready(updateRequestMemAmount);


function toggleLimit(ev) {

	$(ev.target).next('.limit').children().each(function (index, element) {
		$(element).prop("disabled", !$(ev.target).prop("checked"));
	});
}

$('.toggleLimit').change(toggleLimit);

function convert(val, unitA, unitB) {
	if (unitA == unitB)
		return val
	if (unitA == 'GB' && unitB == 'MB')
		return val * 1024;
	if (unitA == 'TB' && unitB == 'MB')
		return val * 1024 * 1024;
	if (unitA == 'hours' && unitB == 'minutes')
		return val * 60;
	if (unitA == 'days' && unitB == 'minutes')
		return val * 60 * 24;
}

function verifyParams(ev) {

	var options = {
		coreNum: $('#coreNum').val(),
		memSize: $('#memSize').val(),
		memUnit: $('#memUnit').val(),

		useWallTime: $('#useWallTime').prop('checked'),
		WallTime: $('#WallTime').val(),

		WallTimeUnit: $('#WallTimeUnit').val(),

		stdout: $('#stdout').val(),
		stderr: $('#stderr').val(),
		script: $('#script').val(),
	}

	$('#verifyDialog').html(`<br> number of cores: ${options.coreNum} <br><br>
	memory per core: ${convert(options.memSize, options.memUnit, 'MB')} MB <br><br>
	total memory: ${convert(options.coreNum*options.memSize, options.memUnit, 'MB')} MB <br><br>
	limit job duration: ${options.useWallTime} <br><br>
	job limit: ${options.useWallTime ? convert(options.WallTime, options.WallTimeUnit, 'minutes') + " minutes" : 'N/A'} <br><br>
	standard out: ${options.stdout} <br><br>
	standard err: ${options.stderr} <br><br>
	path to script: ${options.script} <br><br>
	`);

	$("#verifyDialog").dialog({
		buttons: [{
			text: "Download Script",
			click: function () {
				console.log(getHenryLFS(options));
				$(this).dialog("close");
			}
		}]
	});
}
$('#verifyBtn').click(verifyParams);