TOKEN = '5787955311:AAH4i7W5mt9nosprzyPBEtEfB7NtIwDSNMM'


class Recipe:
    def __init__(self, country, region, profile):
        self.country = country
        self.region = region
        self.profile = profile

    def __str__(self):
        return f'{self.country} | {self.region} | {self.profile}'
