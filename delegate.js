/**
 * Interactive features of index.html are implemented here
 */

// Preview total memory
(function () {
	function updateRequestMemAmount(ev) {
		var coreNum = $('#coreNum').val();
		var memSize = $('#memSize').val();
		var memUnit = $('#memUnit').val();

		res = memSize * coreNum + memUnit;
		$('#totalMemRes').html("Total requested memory is " + res + ".");
	}

	$('#coreNum, #memSize, #memUnit').change(updateRequestMemAmount);
	$(document.body).ready(updateRequestMemAmount);
})();

// Disable unchecked limit parameters
(function () {
	function toggleLimit(ev) {

		$(ev.target).next('.limit').children().each(function (index, element) {
			$(element).prop("disabled", !$(ev.target).prop("checked"));
		});
	}

	$('.toggleLimit').change(toggleLimit);
})();

// Verify and download script
(function () {
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

	function verifyParamsHenry() {
		var options = {
			coreNum: ~~$('#coreNum').val(),
			memSizeMB: ~~convert($('#memSize').val(), $('#memUnit').val(), 'MB'),

			useWallTime: $('#useWallTime').prop('checked'),
			WallTimeMin: ~~convert($('#WallTime').val(), $('#WallTimeUnit').val(), 'minutes'),

			stdout: $('#stdout').val(),
			stderr: $('#stderr').val(),
			exe: $('#script').val(),
		}

		$('#verifyDialog').html(`<br> number of cores: ${options.coreNum} <br><br>
		memory per core: ${options.memSizeMB} MB <br><br>
		total memory: ${options.coreNum*options.memSizeMB} MB <br><br>
		limit job duration: ${options.useWallTime} <br><br>
		job limit: ${options.useWallTime ? options.WallTimeMin + " minutes" : 'N/A'} <br><br>
		standard out: ${options.stdout} <br><br>
		standard err: ${options.stderr} <br><br>
		path to program: ${options.exe} <br><br>
		`);

		$("#verifyDialog").dialog({
			buttons: [{
				text: "Download Script",
				click: function () {
					getHenryLFS(options); //this function is defined in scriptgen.js
					$(this).dialog("close");
				}
			}]
		});
	}

	function verifyParamsLongLeaf() {
		var options = {
			coreNum: ~~$('#coreNum').val(),
			memSizeMB: ~~convert($('#memSize').val(), $('#memUnit').val(), 'MB'),

			useWallTime: $('#useWallTime').prop('checked'),
			WallTimeMin: ~~convert($('#WallTime').val(), $('#WallTimeUnit').val(), 'minutes'),

			stdout: $('#stdout').val(),
			stderr: $('#stderr').val(),
			exe: $('#script').val(),
		}

		$('#verifyDialog').html(`<br> number of cores: ${options.coreNum} <br><br>
		memory per core: ${options.memSizeMB} MB <br><br>
		total memory: ${options.coreNum*options.memSizeMB} MB <br><br>
		limit job duration: ${options.useWallTime} <br><br>
		job limit: ${options.useWallTime ? options.WallTimeMin + " minutes" : 'N/A'} <br><br>
		standard out/err: ${options.stdout} <br><br>
		path to program: ${options.exe} <br><br>
		`);

		$("#verifyDialog").dialog({
			buttons: [{
				text: "Download Script",
				click: function () {
					getCHSlurm(options); //this function is defined in scriptgen.js
					$(this).dialog("close");
				}
			}]
		});
	}

	function verifyParams(ev) {
		if ($('#cluster').val().split(" ")[0].toLowerCase() == "longleaf") {
			verifyParamsLongLeaf(ev);
		} else {
			verifyParamsHenry(ev);
		}
	}
	$('#verifyBtn').click(verifyParams);
})();

// Choose cluster
(function () {
	function chooseCluster(ev) {
		if ($(ev.target).val().split(" ")[0].toLowerCase() == "longleaf") {
			//stdout/stderr
			$('#stderr').prop('disabled', true);
			$('#stderrLongleafHint').show();
		} else {
			$('#stderr').prop('disabled', false);
			$('#stderrLongleafHint').hide();
		}
	}

	$('#cluster').change(chooseCluster)
})();