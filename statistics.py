import pandas as pd

class Statistics:
    def __init__(self, df):
        self.df = pd.DataFrame(df)

    def mean_values(self):
        return self.df.mean()

    def median_values(self):
        return self.df.median()

    def quantiles_values(self, subject='Математика'):
        q1 = self.df[subject].quantile(0.25)
        q3 = self.df[subject].quantile(0.75)
        iqr = q3 - q1
        return {'subject': subject, 'q1': q1, 'q3': q3, 'iqr': iqr}

    def std_values(self):
        return self.df.std()

    def print_values(self, values_list):
        for subject, value in values_list.items():
            print(f"{subject}: {value:.2f}")

    def print_stats(self, subject='Математика'):
        print('Средние значения:')
        self.print_values(self.mean_values())
        print('\nМедианы:')
        self.print_values(self.median_values())
        quantiles = self.quantiles_values(subject)
        print(f"\nКвантили по предмету {quantiles['subject']}:\n"
              f"q1 = {quantiles['q1']}, q3 = {quantiles['q3']}, IQR = {quantiles['iqr']}")
        print('\nСтандартные отклонения:')
        self.print_values(self.std_values())
