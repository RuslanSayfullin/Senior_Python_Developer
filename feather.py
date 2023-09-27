import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather

// Создаем небольшой DataFrame
data = {'A': [1, 2, 3], 'B': ['foo', 'bar', 'baz']}
df = pd.dataFrame(data)

// запиываем DataFrame в файл Feather
feather.write_feather(df, 'example.feather')
