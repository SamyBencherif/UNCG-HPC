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

function getCHSlurm(options) {
	/*
	#!/bin/bash
	#SBATCH --job-name=first_slurm_job //does henry need job names?
	#SBATCH --ntasks=CPU_Count
	#SBATCH --time=Wall_Minutes
	#SBATCH --mem=MB_Per_Core

	python <your python code>
	*/

	//export-file=<filename | fd>

	//SLURM reference https://slurm.schedmd.com/sbatch.html

	/*
	-o, --output=<filename pattern>
	Instruct Slurm to connect the batch script's standard output directly to the file name specified in the
	"filename pattern". By default both standard output and standard error are directed to the same file.
	For job arrays, the default file name is "slurm-%A_%a.out", "%A" is replaced by the job ID and "%a" with
	the array index. For other jobs, the default file name is "slurm-%j.out", where the "%j" is replaced by the
	job ID. See the filename pattern section below for filename specification options.
	*/

	/* Notes
	- stdout/stderr go to the same file
	- what is a job array and do I need to support it?
	*/
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