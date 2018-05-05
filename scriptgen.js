function getHenryLFS(options) {
	var script = "";
	script += `#!/bin/csh\n`
	script += `#BSUB -n ${options.coreNum}										#number of cores\n`

	if (options.useWallTime) {
		script += `#BSUB -W ${options.WallTimeMin}										#Wall time\n`
	}


	script += `#BSUB -R "rusage[mem=${options.memSizeMB}]  span[hosts=1]"		#Memory per core requested ${options.memSizeMB} mb\n`
	script += `source /usr/local/apps/python/python2713.csh\n`
	script += `#BSUB -o ${options.stdout}						#output file location\n`
	script += `#BSUB -e ${options.stderr}						#error file location\n`
	script += `${options.exe}							#code to run`

	// return script;
	download("henry2-config.sh", script);

}

function reverse(k) {
	o = "";
	for (var i = k.length - 1; i > 0; i--)
		o += k[i]
	return o;
}

function getFileName(path) {
	var sep = reverse(path).indexOf('/');
	var dot = reverse(path).indexOf('.');

	return path.substring(sep == -1 ? 0 : path.length - sep, dot == -1 ? path.length : path.length - dot - 1);
}

function getCHSlurm(options) {

	var filename = getFileName(options.exe);

	var script = "";


	script += `#!/bin/bash\n`
	//by default, the job name is based on the no-ext filename of the script
	script += `#SBATCH --job-name=${filename}_slurm_job\n`
	script += `#SBATCH --ntasks=${options.coreNum}\n`
	script += `#SBATCH --time=${options.WallTimeMin}\n`
	script += `#SBATCH --mem=${options.memSizeMB}\n`
	script += `#SBATCH --output=${options.stdout}\n`
	script += `#SBATCH -p general\n`

	script += `python ${options.exe}`

	download("longleaf-config.sh", script);
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