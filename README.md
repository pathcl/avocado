## grid for vsphere it will show you all the alarms!

# to run it locally you need to do:

$ docker run -e 'VSPHERE_VCENTER=yourvcenter.domain.tld' -e 'VSPHERE_USERNAME=username' -e 'VSPHERE_PASSWORD=VSPHERE_PASSWORD' -p 8000:8000 pathcl/grid:0.0.1

Then you'll have it available on http://127.0.0.1:8000
