# Task 3

## pyyaml1

With the env `pyyaml1` we got this result:

```json
{
  'derep': {
    'clustering': 1,
    'length_overlap': 0.0,
    'representative': 'most_common'
  }
}
```

Sadly, we couldn't test pyyaml 3.13, because it wasn't found by conda.
We tried `conda config --add channels conda-forge`, as suggested in the forum on Ilias, but
it still wasn't found.
```bash
% conda env create -f ../../Blätter/Blatt\ 0/data/pyyaml2.yaml
Collecting package metadata (repodata.json): done
Solving environment: failed

ResolvePackageNotFound: 
  - pyyaml=3.13
```