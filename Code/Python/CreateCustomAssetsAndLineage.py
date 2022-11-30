#Lineage for Rapport_Produits report and SalesReport 

import json
import os
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient, AtlasEntity, AtlasProcess,AtlasAttributeDef, EntityTypeDef
from pyapacheatlas.core.typedef import EntityTypeDef
from pyapacheatlas.core.util import GuidTracker


#Add your AAD application as Data Curator in Microsoft Purview Data Catalog
if __name__ == "__main__":
    purview_Account_Name = "PurviewAeffacer"
    oauth = ServicePrincipalAuthentication(
        client_id="53dba755-5f3a-4f32-8046-350f616037a7",
        tenant_id="21b34613-f78a-42f0-8bf9-a7d5bdeb1f03",
        client_secret="QoW8Q~.SrpE3vcVb.sFmQ18MihRLBCjRGNoXeayX"
        )
    client = PurviewClient(
        account_name=purview_Account_Name,
        authentication=oauth
        )
gt = GuidTracker()  


# Create two entities with AtlasEntity
    # You must provide a name, typeName, qualified_name, and guid
    # the guid must be a negative number and unique in your batch
    # being uploaded.
input01 = AtlasEntity(
        name="MyNoteBookForPurview2",
        typeName="DataSet",
        qualified_name="pyapacheatlas://franmerdemoinput01",
        guid=gt.get_guid()
    )
output01 = AtlasEntity(
        name="franmertest",
        typeName="azure_datalake_gen2_resource_set",
        qualified_name="https://stredmslakedev.dfs.core.windows.net/internal/standard/emerald.db/eai_task/{ipl_edm_ingest_date}/{SparkPartitions}",
        guid=gt.get_guid()
    )

    # The Atlas Process is the lineage component that links the two
    # entities together. The inputs and outputs need to be the "header"
    # version of the atlas entities, so specify minimum = True to
    # return just guid, qualifiedName, and typeName.
process = AtlasProcess(
        name="sample process",
        typeName="Process",
        qualified_name="pyapacheatlas://democustomprocess",
        inputs=[input01],
        outputs=[output01],
        guid=gt.get_guid()
    )

    # Convert the individual entities into json before uploading.
results = client.upload_entities(
        batch=[output01, input01, process]
    )

print(json.dumps(results, indent=2))