
def rename_columns(df, func = str.lower, renames = {'dates':'date'}):
    return df.rename(columns=func).rename(columns = renames)

def parse_dates(df, date_col = 'date'):  
    return df.assign(date = lambda df: pd.to_datetime(df[date_col]))

def set_date_as_index(df, date_col='date'):
    return df.set_index(date_col).sort_index()

def filter_date(df, start='2004', end='2014'):
    return df.loc[start:end]

def resample(df, sample_by='ME', col='category', agg_func='count'):
    return df.resample(sample_by)[[col]].agg(agg_func)

def get_rolling(df, window=10, col='category', agg_func='mean'):
    return df.assign(rolling = lambda df: df[col].rolling(window).agg(agg_func))

(
    sanfran
    .pipe(rename_columns)
    .pipe(parse_dates)
    .pipe(set_date_as_index)
    .pipe(filter_date)
    .pipe(resample)
    .pipe(get_rolling)
).plot(figsize=(9,5), title='Crime Count in San Fransisco')