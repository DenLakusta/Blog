
### Using Jmeter in Docker

To run exported from Jmeter test use nxt command

`sudo docker run --name controller --detach --rm --volume \`pwd\`:/jmeter rdpanek/jmeter:latest --nongui --testfile API_GETWAY.jmx --logfile result.jtl -Jhostname=172.18.0.1 -Jport=8080 -Jdataset=input_data.csv --forceDeleteResultFile --reportatendofloadtests --reportoutputfolder report -Jjmeter.reportgenerator.overall_granularity=1000`

`--nongui` - run JMeter in nongui mode
`--testfile` - the jmeter test(.jmx) file to run
`--logfile` - the file to log samples to
`-J --jmeterproperty` - <argument>=<value> Define additional JMeter properties:

	`-Jhostname=172.18.0.1` - can be used in Jmeter `${__P(hostname,)}`
	`-Jport=8080` - can be used in Jmeter test as `${__P(port,)}`
	`Jdataset=input_data.csv` - can be used in Jmeter test as ${__P(dataset,)}
---

