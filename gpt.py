from typing import List, Tuple
import pandas as pd
from collections import OrderedDict

DATE_FORMAT = '%Y-%m-%d'

class FinancialEvent:
    """
    Represents a financial event with a name, start date, and end date.
    """
    def __init__(self, name: str, start_date: pd.Timestamp, end_date: pd.Timestamp) -> None:
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self) -> str:
        return f"FinancialEvent(name='{self.name}', start_date='{self.start_date}', end_date='{self.end_date}')"

    def print_event(self) -> None:
        print(f"Name: {self.name}")
        print(f"Start Date: {self.start_date.strftime(DATE_FORMAT)}")
        print(f"End Date: {self.end_date.strftime(DATE_FORMAT)}")
        print('-' * 50)

def create_financial_events(events_dict: OrderedDict) -> List[FinancialEvent]:
    return [FinancialEvent(name, start_date, end_date) for name, (start_date, end_date) in events_dict.items()]

def main() -> None:
    financial_events_dict = OrderedDict([
        ('Dotcom', (pd.Timestamp('20000310'), pd.Timestamp('20000910'))),
        ('Lehman', (pd.Timestamp('20080801'), pd.Timestamp('20081001'))),
        ('9/11', (pd.Timestamp('20010911'), pd.Timestamp('20011011'))),
        ('US downgrade/European Debt Crisis', (pd.Timestamp('20110805'), pd.Timestamp('20110905'))),
        ('Fukushima', (pd.Timestamp('20110316'), pd.Timestamp('20110416'))),
        ('US Housing', (pd.Timestamp('20030108'), pd.Timestamp('20030208'))),
        ('EZB IR Event', (pd.Timestamp('20120910'), pd.Timestamp('20121010'))),
        ('Aug07', (pd.Timestamp('20070801'), pd.Timestamp('20070901'))),
        ('Mar08', (pd.Timestamp('20080301'), pd.Timestamp('20080401'))),
        ('Sept08', (pd.Timestamp('20080901'), pd.Timestamp('20081001'))),
        ('2009Q1', (pd.Timestamp('20090101'), pd.Timestamp('20090301'))),
        ('2009Q2', (pd.Timestamp('20090301'), pd.Timestamp('20090601'))),
        ('Flash Crash', (pd.Timestamp('20100505'), pd.Timestamp('20100510'))),
        ('Apr14', (pd.Timestamp('20140401'), pd.Timestamp('20140501'))),
        ('Oct14', (pd.Timestamp('20141001'), pd.Timestamp('20141101'))),
        ('Fall2015', (pd.Timestamp('20150815'), pd.Timestamp('20150930'))),
        ('Low Volatility Bull Market', (pd.Timestamp('20050101'), pd.Timestamp('20070801'))),
        ('GFC Crash', (pd.Timestamp('20050101'), pd.Timestamp('20070801'))),
        ('Recovery', (pd.Timestamp('20050101'), pd.Timestamp('20070801'))),
        ('New Normal', (pd.Timestamp('20050101'), pd.Timestamp('20070801')))
    ])

    financial_events = create_financial_events(financial_events_dict)

    for event in financial_events:
        event.print_event()

if __name__ == "__main__":
    main()
