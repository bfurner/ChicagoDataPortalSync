import ChicagoDataPortal.DataSetMetadata
import requests
import ExportSettings as es


chicagodatasets = requests.get(es.BASE_METADATA_URI)

items = ChicagoDataPortal.DataSetMetadata.DataSetList(datasets = chicagodatasets.text)

for dataset in items.datasets:
    dataset_was_updated = False if dataset.dataUpdatedAt == None else dataset.dataUpdatedAt > es.LAST_RUN
    if dataset_was_updated:
        print(dataset.id + ': ' + str(dataset.dataUpdatedAt))
        dataset_download_req = requests.get(es.BASE_RESOURCE_URI + dataset.id + ".json")
        with open(es.OUTPUT_DIR + dataset.id + ".json", "w") as outfile:
            outfile.write(dataset_download_req.text)
