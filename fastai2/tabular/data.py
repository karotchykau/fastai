# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/41_tabular.data.ipynb (unless otherwise specified).

__all__ = ['TabularDataBunch']

# Cell
from ..torch_basics import *
from ..data.all import *
from .core import *

# Cell
class TabularDataBunch(DataBunch):
    @classmethod
    @delegates(Tabular.databunch)
    def from_df(cls, df, path='.', procs=None, cat_names=None, cont_names=None, y_names=None, block_y=CategoryBlock,
                valid_idx=None, **kwargs):
        if cat_names is None: cat_names = []
        if cont_names is None: cont_names = list(set(df)-set(cat_names)-set(y_names))
        splits = RandomSplitter()(df) if valid_idx is None else IndexSplitter(valid_idx)(df)
        to = TabularPandas(df, procs, cat_names, cont_names, y_names, splits=splits, block_y=block_y)
        return to.databunch(path=path, **kwargs)

    @classmethod
    @delegates(Tabular.databunch)
    def from_csv(cls, csv, path='.', procs=None, cat_names=None, cont_names=None, y_names=None, block_y=CategoryBlock,
                valid_idx=None, **kwargs):
        return cls.from_df(pd.read_csv(csv), path, procs, cat_names=cat_names, cont_names=cont_names, y_names=y_names,
                           block_y=block_y, valid_idx=valid_idx, **kwargs)