#!/bin/bash
#
# Copyright (c) 2014-2015 Oracle and/or its affiliates. All rights reserved.
#

# If log.nm does not exists, container is starting for 1st time
# So it should start NM and also associate with AdminServer, as well Managed Server
# Otherwise, only start NM (container is being restarted)
if [ ! -f log.nm ]; then
    ADD_SERVER=1
fi

# Wait for AdminServer to become available for any subsequent operation
/u01/oracle/waitForAdminServer.sh

# Start Node Manager
echo "Starting NodeManager in background..."
nohup startNodeManager.sh > log.nm 2>&1 &
echo "NodeManager started."
echo $XML
adminURL=$(python -c 'import xmlUtil; print xmlUtil.getAdminURL()')
echo $adminURL

#managedServers=$(python -c 'import xmlUtil; print xmlUtil.getManagedServers()')
#IFS=, read -r -a managedServerArr <<< "$managedServers"
#for element in "${managedServerArr[@]}"
#do
# echo "$element"
#done

datasources=$(python -c 'import xmlUtil; print xmlUtil.getDatasources()')
IFS=, read -r -a datasourceArr <<< "$datasources"
for element in "${datasourceArr[@]}"
do
 datasourceDetailString=$(python -c "import xmlUtil; print xmlUtil.getDatasourceDetails('${element}')")
 IFS=, read -r -a datasourceDetailArr <<< "$datasourceDetailString"
 wlst /u01/oracle/create_data_source.py "${datasourceDetailArr[0]}" "${datasourceDetailArr[1]}" "${datasourceDetailArr[2]}" "${datasourceDetailArr[3]}" "${datasourceDetailArr[4]}" "${datasourceDetailArr[5]}" "${datasourceDetailArr[6]}" "${datasourceDetailArr[7]}" "${datasourceDetailArr[8]}" "${datasourceDetailArr[9]}" "${datasourceDetailArr[10]}"
done 

# print log
#tail -f log.nm /u01/oracle/user_projects/domains/$DOMAIN_NAME/servers/*/logs/*.out
