function getHenryLFS(options) {
	var script = "";
	script += `#!/bin/csh\n`
	script += `#BSUB -n ${options.coreNum}										#number of cores\n`

	if (options.useWallTime) {
		script += `#BSUB -W ${options.WallTimeMin}										#Wall time\n`
	}


	script += `#BSUB -R "rusage[mem=${options.memSizeMB}]  span[hosts=1]"		#Memory per core requested ${convert(options.memSize, options.memUnit, 'MB')} mb\n`
	script += `source /usr/local/apps/python/python2713.csh\n`
	script += `#BSUB -o ${options.stdout}						#output file location\n`
	script += `#BSUB -e ${options.stderr}						#error file location\n`
	script += `${options.script}							#code to run`

	// return script;
	download("run.sh", script);

}

//thank you https://ourcodeworld.com/articles/read/189/how-to-create-a-file-and-generate-a-download-with-javascript-in-the-browser-without-a-server
function download(filename, text) {
	var element = document.createElement('a');
	element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
	element.setAttribute('download', filename);

	element.style.display = 'none';
	document.body.appendChild(element);

	element.click();

	document.body.removeChild(element);
}