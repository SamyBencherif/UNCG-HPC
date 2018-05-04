function getHenryLFS(options) {
	var script = "";
	script += `#!/bin/csh\n`
	script += `#BSUB -n ${options.coreNum}										#number of cores\n`

	if (options.useWallTime) {
		script += `#BSUB -W ${convert(options.WallTime, options.WallTimeUnit, 'minutes')}										#Wall time\n`
	}


	script += `#BSUB -R "rusage[mem=${convert(options.memSize, options.memUnit, 'MB')}]  span[hosts=1]"		#Memory per core requested ${convert(options.memSize, options.memUnit, 'MB')} mb\n`
	script += `source /usr/local/apps/python/python2713.csh\n`
	script += `#BSUB -o ${options.stdout}						#output file location\n`
	script += `#BSUB -e ${options.stderr}						#error file location\n`
	script += `${options.script}							#code to run`

	return script;
}