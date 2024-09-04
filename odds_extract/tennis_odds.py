import json_loading
import datetime
from datetime import date
import pandas as pd
import sideFunctions


def fetch_tennis_odds_mozzartbet():
    today = date.today()


    payload_bet_offer_tennis = {
        "date": "all",
        "sportIds": [
            5
        ],
        "competitionIds": [],
        "sort": "bytime",
        "specials": False,
        "subgames": [],
        "size": 200,
        "mostPlayed": False,
        "type": "betting",
        "numberOfGames": 0,
        "activeCompleteOffer": False,
        "lang": "sr",
        "offset": 0
    }

    tennis_bet_offer = json_loading.load_json_get("https://www.mozzartbet.com/betOffer2", payload_bet_offer_tennis)

    #no_of_matches = tennis_bet_offer['total']
    s = tennis_bet_offer['matches']

    match_id_list = []
    home_team_names_list = []
    guest_team_names_list = []
    league_list = []
    provider = []
    kickoff_time_list = []
    ki1_list = []
    ki2_list = []
    h1_list = []
    h2_list = []
    first_set_home_list = []
    first_set_away_list = []
    three_sets_list = []
    two_sets_list = []
    first_set_under_11 = []
    first_set_11_or_over = []
    first_set_under_10 = []
    first_set_10_or_over = []
    first_set_under_9 = []
    first_set_9_or_over = []
    first_set_under_8 = []
    first_set_8_or_over = []
    second_set_under_10 = []
    second_set_10_or_over = []
    second_set_under_9 = []
    second_set_9_or_over = []
    second_set_under_8 = []
    second_set_8_or_over = []

    for match in s:
        match_id_list.append(match['id'])

        try:
            first_player_name = match['participants'][0]['name']
            second_player_name = match['participants'][1]['name']
            result = json_loading.loadPlayerNameBasedOnMatch(first_player_name + '-' + second_player_name)
            first_name, second_name = result.split('-')
            home_team_names_list.append(first_name)
            guest_team_names_list.append(second_name)
        except:
            home_team_names_list.append(match['participants'][0]['name'])
            guest_team_names_list.append(match['participants'][1]['name'])

        league_list.append(match['competition_name_sr'])
        timestamp_ms = match['startTime']
        timestamp_s = timestamp_ms / 1000  # Convert milliseconds to seconds
        kick_off_time = datetime.datetime.utcfromtimestamp(timestamp_s)
        one_hour = datetime.timedelta(hours=1)
        kick_off_time += one_hour
        kickoff_time_list.append(kick_off_time)
        provider.append('MOZZARTBET')

    for match_id in match_id_list:
        match_tennis_payload = {"id": match_id,
                        "subgames": [1005017001, 1005017003, 1005001001, 1005001003, 1005022001, 1005022002, 1005086001, 1005086002,
                                 1005138001, 1005138002, 1005138003, 1005138004, 1005138005, 1005138006, 1005152001,1005152002,
                                 1005152003, 1005152004, 1005152005, 1005152006]}

        match_odds = json_loading.load_json_post("https://www.mozzartbet.com/matchBetting", match_tennis_payload)

        ##try:
        ##    ki1, ki2, first_set_ki1, first_set_ki2 = json_loading.loadOddsFromSofaScore(
        #        home_team_names_list[i] + '-' + guest_team_names_list[i])
        #except:
        #    ki1, ki2, first_set_ki1, first_set_ki2 = 'Null', 'Null', 'Null', 'Null'

        #if ki1 != 'Null' and ki2 != 'Null':
        #    numerator_1, denominator_1 = map(int, ki1.split('/'))
        #    numerator_2, denominator_2 = map(int, ki2.split('/'))

        #    ki1_f = round(numerator_1 / denominator_1 + 1,2)
        #    ki2_f = round(numerator_2 / denominator_2 + 1, 2)
        #    ki1_list.append(ki1_f)
        #    ki2_list.append(ki2_f)
        #else:
        ki1_list.append(match_odds['kodds']['1005017001']['value'])
        ki2_list.append(match_odds['kodds']['1005017003']['value'])

        try:
            h1_list.append(match_odds['kodds']['1005001001']['value'])
        except:
            h1_list.append('-1')

        try:
            h2_list.append(match_odds['kodds']['1005001003']['value'])
        except:
            h2_list.append('-1')

        try:
            first_set_home_list.append(match_odds['kodds']['1005022001']['value'])
        except:
            first_set_home_list.append('-1')

        try:
            first_set_away_list.append(match_odds['kodds']['1005022002']['value'])
        except:
            first_set_away_list.append('-1')

        try:
            two_sets_list.append(match_odds['kodds']['1005086001']['value'])
        except:
            two_sets_list.append('-1')

        try:
            three_sets_list.append(match_odds['kodds']['1005086002']['value'])
        except:
            three_sets_list.append('-1')

        try:
            first_set_under_10.append(match_odds['kodds']['1005138001']['value'])
        except:
            first_set_under_10.append('-1')

        try:
            first_set_10_or_over.append(match_odds['kodds']['1005138002']['value'])
        except:
            first_set_10_or_over.append('-1')

        try:
            first_set_under_9.append(match_odds['kodds']['1005138003']['value'])
        except:
            first_set_under_9.append('-1')

        try:
            first_set_9_or_over.append(match_odds['kodds']['1005138004']['value'])
        except:
            first_set_9_or_over.append('-1')

        try:
            first_set_under_8.append(match_odds['kodds']['1005138005']['value'])
        except:
            first_set_under_8.append('-1')

        try:
            first_set_8_or_over.append(match_odds['kodds']['1005138006']['value'])
        except:
            first_set_8_or_over.append('-1')

        try:
            second_set_under_10.append(match_odds['kodds']['1005152001']['value'])
        except:
            second_set_under_10.append('-1')

        try:
            second_set_10_or_over.append(match_odds['kodds']['1005152002']['value'])
        except:
            second_set_10_or_over.append('-1')

        try:
            second_set_under_9.append(match_odds['kodds']['1005152003']['value'])
        except:
            second_set_under_9.append('-1')

        try:
            second_set_9_or_over.append(match_odds['kodds']['1005152004']['value'])
        except:
            second_set_9_or_over.append('-1')

        try:
            second_set_under_8.append(match_odds['kodds']['1005152005']['value'])
        except:
            second_set_under_8.append('-1')

        try:
            second_set_8_or_over.append(match_odds['kodds']['1005152006']['value'])
        except:
            second_set_8_or_over.append('-1')

        first_set_under_11.append('-1')
        first_set_11_or_over.append('-1')

    headers = ["provider", "kick_off", "league", "home_name", "away_name", "ki1", "ki2", "ts2", "ts3", "firstSet1", "firstSet2", "1s <10,5", "1s 11+", "1s <9,5", "1s 10+", "1s <8,5", "1s 9+", "1s <7,5", "1s 8+",
           "2s <9,5", "2s 10+", "2s <8,5", "2s 9+", "2s <7,5", "2s 8+"]

    zipped = list(zip(provider, kickoff_time_list,league_list, home_team_names_list, guest_team_names_list, ki1_list, ki2_list, two_sets_list, three_sets_list,
                  first_set_home_list, first_set_away_list, first_set_under_11, first_set_11_or_over,
                  first_set_under_10, first_set_10_or_over, first_set_under_9, first_set_9_or_over, first_set_under_8, first_set_8_or_over,
                  second_set_under_10, second_set_10_or_over, second_set_under_9, second_set_9_or_over, second_set_under_8, second_set_8_or_over))

    df = pd.DataFrame(zipped, columns=headers)
    df['ki1'] = df['ki1'].astype('float64')
    df['ki2'] = df['ki2'].astype('float64')
    df['firstSet1'] = df['firstSet1'].astype('float64')
    df['firstSet2'] = df['firstSet2'].astype('float64')
    df['ts2'] = df['ts2'].astype('float64')
    df['ts3'] = df['ts3'].astype('float64')
    df['1s <10,5'] = df['1s <10,5'].astype('float64')
    df['1s <9,5'] = df['1s <9,5'].astype('float64')
    df['1s <8,5'] = df['1s <8,5'].astype('float64')
    df['1s <7,5'] = df['1s <7,5'].astype('float64')
    df['2s <9,5'] = df['2s <9,5'].astype('float64')
    df['2s <8,5'] = df['2s <8,5'].astype('float64')
    df['2s <7,5'] = df['2s <7,5'].astype('float64')
    df['1s 11+'] = df['1s 11+'].astype('float64')
    df['1s 10+'] = df['1s 10+'].astype('float64')
    df['1s 9+'] = df['1s 9+'].astype('float64')
    df['1s 8+'] = df['1s 8+'].astype('float64')
    df['2s 10+'] = df['2s 10+'].astype('float64')
    df['2s 9+'] = df['2s 9+'].astype('float64')
    df['2s 8+'] = df['2s 8+'].astype('float64')
    return df


def fetch_tennis_odds_soccerbet():
    url = "https://www.soccerbet.rs/restapi/offer/sr/sport/T/mob"
    query_params = {
        "annex": "0",
        "mobileVersion": "2.27.13",
        "locale": "sr"
    }

    s = json_loading.load_json_url(url, query_params)

    match_id_list = []
    home_name_list = []
    away_name_list = []
    kickoff_time_list = []
    league_name_list = []
    provider = []

    for match in s['esMatches']:
        if match['live'] == 'true':
            continue
        else:
            match_id_list.append(match['id'])
            #if '/' in match['home']:
            #    parts = match['home'].split('/')
            #    try:
            #        a = json_loading.loadPlayerName(parts[0])
            #        b = json_loading.loadPlayerName(parts[1])
            #        home_name_list.append(a + "/" + b)
            #    except:
            #        home_name_list.append(json_loading.loadPlayerName(match['home']))

            #if '/' in match['away']:
            #    parts = match['away'].split('/')
            #    try:
            #        c = json_loading.loadPlayerName(parts[0])
            #        d = json_loading.loadPlayerName(parts[1])
            #        away_name_list.append(c + "/" + d)
            #    except:
            #       away_name_list.append(json_loading.loadPlayerName(match['away']))

            #else:
            #    try:
            #        a = json_loading.loadPlayerName(match['home'])
            #        b = json_loading.loadPlayerName(match['away'])
            #        if a == 'Djokovic Marko':
            #            a = 'Djokovic Novak'
            #        elif b == 'Djokovic Marko':
            #            b = 'Djokovic Novak'
            #        home_name_list.append(a)
            #        away_name_list.append(b)
            #    except:
            #        home_name_list.append(json_loading.loadPlayerName(match['home']))
            #        away_name_list.append(json_loading.loadPlayerName(match['away']))
            try:
                result = json_loading.loadPlayerNameBasedOnMatch(match['home'] + '-' + match['away'])
                first_name, second_name = result.split('-')
                home_name_list.append(first_name)
                away_name_list.append(second_name)
            except:
                home_name_list.append(match['home'])
                away_name_list.append(match['away'])
            timestamp_ms = match['kickOffTime']
            timestamp_s = timestamp_ms / 1000  # Convert milliseconds to seconds
            kick_off_time = datetime.datetime.utcfromtimestamp(timestamp_s)
            one_hour = datetime.timedelta(hours=1)
            kick_off_time += one_hour
            kickoff_time_list.append(kick_off_time)
            league_name_list.append(match['leagueName'])
            provider.append('SOCCERBET')

    ki1_list = []
    ki2_list = []
    h1_list = []
    h2_list = []
    first_set_home_list = []
    first_set_away_list = []
    three_sets_list = []
    two_sets_list = []
    first_set_11_or_over = []
    first_set_under_11 = []
    first_set_under_10 = []
    first_set_10_or_over = []
    first_set_under_9 = []
    first_set_9_or_over = []
    first_set_under_8 = []
    first_set_8_or_over = []
    second_set_under_10 = []
    second_set_10_or_over = []
    second_set_under_9 = []
    second_set_9_or_over = []
    second_set_under_8 = []
    second_set_8_or_over = []

    for match_id in match_id_list:
        match_url = f"https://www.soccerbet.rs/restapi/offer/sr/match/{match_id}"
        match_odds = json_loading.load_json_url(match_url, query_params)

        ki1_list.append(match_odds['betMap']['1']['NULL']['ov'])
        ki2_list.append(match_odds['betMap']['3']['NULL']['ov'])

        try:
            three_sets_list.append(match_odds['betMap']['261']['variant=sr:exact_sets:bestof:3']['ov'])
        except:
            try:
                three_sets_list.append(match_odds['betMap']['51448']['total=2.5']['ov'])
            except:
                three_sets_list.append('-1')

        try:
            two_sets_list.append(match_odds['betMap']['260']['variant=sr:exact_sets:bestof:3']['ov'])
        except:
            try:
                two_sets_list.append(match_odds['betMap']['51447']['total=2.5']['ov'])
            except:
                two_sets_list.append('-1')

        try:
            first_set_home_list.append(match_odds['betMap']['201046']['setnr=1']['ov'])
        except:
            try:
                first_set_home_list.append(match_odds['betMap']['50510']['NULL']['ov'])
            except:
                first_set_home_list.append('-1')

        try:
            first_set_away_list.append(match_odds['betMap']['201047']['setnr=1']['ov'])
        except:
            try:
                first_set_away_list.append(match_odds['betMap']['50511']['NULL']['ov'])
            except:
                first_set_away_list.append('-1')

        try:
            first_set_11_or_over.append(match_odds['betMap']['259']["total=10.5"]['ov'])
        except:
            try:
                first_set_11_or_over.append(match_odds['betMap']['201050']['setnr=1,total=10.5']['ov'])
            except:
                first_set_11_or_over.append('-1')

        try:
            first_set_10_or_over.append(match_odds['betMap']['259']["total=9.5"]['ov'])
        except:
            try:
                first_set_10_or_over.append(match_odds['betMap']['201050']['setnr=1,total=9.5']['ov'])
            except:
                first_set_10_or_over.append('-1')

        try:
            first_set_9_or_over.append(match_odds['betMap']['259']["total=8.5"]['ov'])
        except:
            try:
                first_set_9_or_over.append(match_odds['betMap']['201050']['setnr=1,total=8.5']['ov'])
            except:
                first_set_9_or_over.append('-1')

        try:
            first_set_8_or_over.append(match_odds['betMap']['259']["total=7.5"]['ov'])
        except:
            try:
                first_set_8_or_over.append(match_odds['betMap']['201050']['setnr=1,total=7.5']['ov'])
            except:
                first_set_8_or_over.append('-1')

        try:
            first_set_under_11.append(match_odds['betMap']['257']["total=10.5"]['ov'])
        except:
            try:
                first_set_under_11.append(match_odds['betMap']['201051']['setnr=1,total=10.5']['ov'])
            except:
                first_set_under_11.append('-1')

        try:
            first_set_under_10.append(match_odds['betMap']['257']["total=9.5"]['ov'])
        except:
            try:
                first_set_under_10.append(match_odds['betMap']['201051']['setnr=1,total=9.5']['ov'])
            except:
                first_set_under_10.append('-1')

        try:
            first_set_under_9.append(match_odds['betMap']['257']["total=8.5"]['ov'])
        except:
            try:
                first_set_under_9.append(match_odds['betMap']['201051']['setnr=1,total=8.5']['ov'])
            except:
                first_set_under_9.append('-1')

        try:
            first_set_under_8.append(match_odds['betMap']['257']["total=7.5"]['ov'])
        except:
            try:
                first_set_under_8.append(match_odds['betMap']['201051']['setnr=1,total=7.5']['ov'])
            except:
                first_set_under_8.append('-1')

        try:
            second_set_10_or_over.append(match_odds['betMap']['50521']["total=9.5"]['ov'])
        except:
            second_set_10_or_over.append('-1')

        try:
            second_set_under_10.append(match_odds['betMap']['50520']["total=9.5"]['ov'])
        except:
            second_set_under_10.append('-1')

        try:
            second_set_9_or_over.append(match_odds['betMap']['50521']["total=8.5"]['ov'])
        except:
            second_set_9_or_over.append('-1')

        try:
            second_set_under_9.append(match_odds['betMap']['50520']["total=8.5"]['ov'])
        except:
            second_set_under_9.append('-1')

        try:
            second_set_under_8.append(match_odds['betMap']['50520']["total=7.5"]['ov'])
        except:
            second_set_under_8.append('-1')

        try:
            second_set_8_or_over.append(match_odds['betMap']['50521']["total=7.5"]['ov'])
        except:
            second_set_8_or_over.append('-1')

    headers = ["provider", "kick_off", "league", "home_name", "away_name", "ki1", "ki2", "ts2", "ts3", "firstSet1", "firstSet2",
               "firstSet_u_10_5", "firstSet_o_11",
               "firstSet_u_9_5", "firstSet_o_10", "firstSet_u_8_5", "firstSet_o_9", "firstSet_u_7_5", "firstSet_o_8",
               "2s <9,5", "2s 10+", "2s <8,5", "2s 9+", "2s <7,5", "2s 8+"]

    zipped = list(zip(provider, kickoff_time_list, league_name_list, home_name_list, away_name_list, ki1_list, ki2_list,two_sets_list,three_sets_list,
                      first_set_home_list, first_set_away_list,
                      first_set_under_11, first_set_11_or_over,
                      first_set_under_10, first_set_10_or_over, first_set_under_9, first_set_9_or_over, first_set_under_8, first_set_8_or_over,
                      second_set_under_10, second_set_10_or_over, second_set_under_9, second_set_9_or_over, second_set_under_8, second_set_8_or_over))

    df = pd.DataFrame(zipped, columns=headers)
    df['ki1'] = df['ki1'].astype('float64')
    df['ki2'] = df['ki2'].astype('float64')
    df['firstSet1'] = df['firstSet1'].astype('float64')
    df['firstSet2'] = df['firstSet2'].astype('float64')
    df['ts2'] = df['ts2'].astype('float64')
    df['ts3'] = df['ts3'].astype('float64')
    df['firstSet_u_10_5'] = df['firstSet_u_10_5'].astype('float64')
    df['firstSet_u_9_5'] = df['firstSet_u_9_5'].astype('float64')
    df['firstSet_u_8_5'] = df['firstSet_u_8_5'].astype('float64')
    df['firstSet_u_7_5'] = df['firstSet_u_7_5'].astype('float64')
    df['2s <9,5'] = df['2s <9,5'].astype('float64')
    df['2s <8,5'] = df['2s <8,5'].astype('float64')
    df['2s <7,5'] = df['2s <7,5'].astype('float64')
    df['firstSet_o_11'] = df['firstSet_o_11'].astype('float64')
    df['firstSet_o_10'] = df['firstSet_o_10'].astype('float64')
    df['firstSet_o_9'] = df['firstSet_o_9'].astype('float64')
    df['firstSet_o_8'] = df['firstSet_o_8'].astype('float64')
    df['2s 10+'] = df['2s 10+'].astype('float64')
    df['2s 9+'] = df['2s 9+'].astype('float64')
    df['2s 8+'] = df['2s 8+'].astype('float64')

    return df


def fetch_maxbet_odds():
    s = json_loading.load_leagues_list_maxbet(
        'https://www.maxbet.rs/restapi/offer/sr/categories/sport/T/l?annex=3&desktopVersion=2.30.10&locale=sr')

    league_ids_list = []
    league_list = []
    for categorie in s['categories']:
        league_list.append(categorie['name'])
        league_ids_list.append(categorie['id'])

    home_team_names_list = []
    guest_team_names_list = []
    provider = []
    kickoff_time_list = []
    ki1_list = []
    ki2_list = []
    h1_list = []
    h2_list = []
    first_set_home_list = []
    first_set_away_list = []
    three_sets_list = []
    two_sets_list = []
    first_set_under_11 = []
    first_set_11_or_over = []
    first_set_under_10 = []
    first_set_10_or_over = []
    first_set_under_9 = []
    first_set_9_or_over = []
    first_set_under_8 = []
    first_set_8_or_over = []
    second_set_under_10 = []
    second_set_10_or_over = []
    second_set_under_9 = []
    second_set_9_or_over = []
    second_set_under_8 = []
    second_set_8_or_over = []
    matches_ids_list_df = []
    league_names_list = []

    for id in league_ids_list:
        f = json_loading.load_matches_list_maxbet(
            f'https://www.maxbet.rs/restapi/offer/sr/sport/T/league/{id}/mob?annex=3&desktopVersion=2.30.10&locale=sr')
        matches_ids_list = []


        for match in f['esMatches']:
            matches_ids_list.append(match['id'])
            matches_ids_list_df.append(match['id'])

        for match in matches_ids_list:
            a = json_loading.load_odds_maxbet(
                f'https://www.maxbet.rs/restapi/offer/sr/match/{match}?annex=3&desktopVersion=2.30.10&locale=sr')

            #if '/' in a['home']:
            #    parts = a['home'].split('/')
            #    try:
            #        e = json_loading.loadPlayerName(parts[0])
            #        r = json_loading.loadPlayerName(parts[1])
            #        home_team_names_list.append(e + "/" + r)
            #    except:
            #        home_team_names_list.append(a['home'])
            #elif '/' in a['away']:
            #    parts = a['home'].split('/')
            #    try:
            #        c = json_loading.loadPlayerName(parts[0])
            #        d = json_loading.loadPlayerName(parts[1])
            #        guest_team_names_list.append(c + "/" + d)
            #    except:
            #        guest_team_names_list.append(a['away'])
            #else:
            #    try:
            #        e = json_loading.loadPlayerName(a['home'])
            #        r = json_loading.loadPlayerName(a['away'])
            #        if e == 'Djokovic Marko':
            #            e = 'Djokovic Novak'
            #        elif r == 'Djokovic Marko':
            #            r = 'Djokovic Novak'
            #        home_team_names_list.append(e)
            #        guest_team_names_list.append(r)
            #    except:
            #        home_team_names_list.append(a['home'])
            #        guest_team_names_list.append(a['away'])
            try:
                result = json_loading.loadPlayerNameBasedOnMatch(a['home'] + '-' + a['away'])
                first_name, second_name = result.split('-')
                home_team_names_list.append(first_name)
                guest_team_names_list.append(second_name)
            except:
                home_team_names_list.append(a['home'])
                guest_team_names_list.append(a['away'])
            league_names_list.append(f['name'])

            timestamp_ms = a['kickOffTime']
            timestamp_s = timestamp_ms / 1000  # Convert milliseconds to seconds
            kick_off_time = datetime.datetime.utcfromtimestamp(timestamp_s)
            two_hours_addition = datetime.timedelta(hours=2)
            kick_off_time += two_hours_addition
            kickoff_time_list.append(kick_off_time)

            try:
                ki1_list.append(a['odds']['1'])
            except:
                ki1_list.append('-1')

            try:
                ki2_list.append(a['odds']['3'])
            except:
                ki2_list.append('-1')

            try:
                first_set_home_list.append(a['odds']['50512'])
            except:
                first_set_home_list.append('-1')

            try:
                first_set_away_list.append(a['odds']['50513'])
            except:
                first_set_away_list.append('-1')

            try:
                three_sets_list.append(a['odds']['261'])
            except:
                three_sets_list.append('-1')

            try:
                two_sets_list.append(a['odds']['260'])
            except:
                two_sets_list.append('-1')

            try:
                first_set_under_11.append(a['odds']['51373'])
            except:
                first_set_under_11.append('-1')

            try:
                first_set_11_or_over.append(a['odds']['51375'])
            except:
                first_set_11_or_over.append('-1')

            try:
                first_set_9_or_over.append(a['odds']['51372'])
            except:
                first_set_9_or_over.append('-1')

            try:
                first_set_under_9.append(a['odds']['51370'])
            except:
                first_set_under_9.append('-1')

            try:
                first_set_under_8.append(a['odds']['51376'])
            except:
                first_set_under_8.append('-1')

            try:
                first_set_8_or_over.append(a['odds']['51378'])
            except:
                first_set_8_or_over.append('-1')

            try:
                first_set_10_or_over.append(a['odds']['259'])
            except:
                first_set_10_or_over.append('-1')

            try:
                first_set_under_10.append(a['odds']['257'])
            except:
                first_set_under_10.append('-1')

            try:
                second_set_under_10.append(a['odds']['50520'])
            except:
                second_set_under_10.append('-1')

            try:
                second_set_10_or_over.append(a['odds']['50521'])
            except:
                second_set_10_or_over.append('-1')

            second_set_under_9.append('-1')
            second_set_9_or_over.append('-1')
            second_set_under_8.append('-1')
            second_set_8_or_over.append('-1')
            provider.append('MaxBet')
            h1_list.append('-1')
            h2_list.append('1')

    headers = ["provider", "kick_off", "league", "home_name", "away_name", "ki1", "ki2", "ts2", "ts3", "firstSet1",
               "firstSet2",
               "firstSet_u_10_5", "firstSet_o_11",
               "firstSet_u_9_5", "firstSet_o_10", "firstSet_u_8_5", "firstSet_o_9", "firstSet_u_7_5", "firstSet_o_8",
               "secondSet <9,5", "secondSet 10+", "secondSet <8,5", "secondSet 9+", "secondSet <7,5", "secondSet 8+"]

    zipped = list(
        zip(provider, kickoff_time_list, league_names_list, home_team_names_list, guest_team_names_list, ki1_list, ki2_list,
            two_sets_list,
            three_sets_list,
            first_set_home_list, first_set_away_list, first_set_under_11, first_set_11_or_over,
            first_set_under_10, first_set_10_or_over, first_set_under_9, first_set_9_or_over,
            first_set_under_8, first_set_8_or_over,
            second_set_under_10, second_set_10_or_over, second_set_under_9, second_set_9_or_over,
            second_set_under_8, second_set_8_or_over))

    df = pd.DataFrame(zipped, columns=headers)
    df['ki1'] = df['ki1'].astype('float64')
    df['ki2'] = df['ki2'].astype('float64')
    df['firstSet1'] = df['firstSet1'].astype('float64')
    df['firstSet2'] = df['firstSet2'].astype('float64')
    df['ts2'] = df['ts2'].astype('float64')
    df['ts3'] = df['ts3'].astype('float64')
    df['firstSet_u_10_5'] = df['firstSet_u_10_5'].astype('float64')
    df['firstSet_u_9_5'] = df['firstSet_u_9_5'].astype('float64')
    df['firstSet_u_8_5'] = df['firstSet_u_8_5'].astype('float64')
    df['firstSet_u_7_5'] = df['firstSet_u_7_5'].astype('float64')
    df['secondSet <9,5'] = df['secondSet <9,5'].astype('float64')
    df['secondSet <8,5'] = df['secondSet <8,5'].astype('float64')
    df['secondSet <7,5'] = df['secondSet <7,5'].astype('float64')
    df['firstSet_o_11'] = df['firstSet_o_11'].astype('float64')
    df['firstSet_o_10'] = df['firstSet_o_10'].astype('float64')
    df['firstSet_o_9'] = df['firstSet_o_9'].astype('float64')
    df['firstSet_o_8'] = df['firstSet_o_8'].astype('float64')
    df['secondSet 10+'] = df['secondSet 10+'].astype('float64')
    df['secondSet 9+'] = df['secondSet 9+'].astype('float64')
    df['secondSet 8+'] = df['secondSet 9+'].astype('float64')

    return df


def fetch_superbet_odds():
    tournaments_json = json_loading.get_tournaments_suberbet(
        'https://production-superbet-offer-rs.freetls.fastly.net/sb-rs/api/v2/sr-Latn-RS/sport/2/tournaments')

    tournaments_ids_list = []
    tournaments_names_list = []
    match_ids_list = []
    home_team_names_list = []
    guest_team_names_list = []
    provider = []
    kickoff_time_list = []
    ki1_list = []
    ki2_list = []
    h1_list = []
    h2_list = []
    first_set_home_list = []
    first_set_away_list = []
    three_sets_list = []
    two_sets_list = []
    first_set_under_11 = []
    first_set_11_or_over = []
    first_set_under_10 = []
    first_set_10_or_over = []
    first_set_under_9 = []
    first_set_9_or_over = []
    first_set_under_8 = []
    first_set_8_or_over = []
    second_set_under_10 = []
    second_set_10_or_over = []
    second_set_under_9 = []
    second_set_9_or_over = []
    second_set_under_8 = []
    second_set_8_or_over = []
    matches_ids_list_df = []
    league_names_list = []
    for tournaments in tournaments_json['data']:
        for competition in tournaments['competitions']:
            tournaments_ids_list.append(competition['tournamentId'])
            tournaments_names_list.append(competition['localNames']['sr-Latn-RS'])
    print('prvi deo')
    for tournament in tournaments_ids_list:
        matches = json_loading.get_matches_suberbet(tournament)
        for match in matches['data']:
            match_ids_list.append(match['eventId'])
            try:
                names = json_loading.loadPlayerNameBasedOnMatch(match['matchName'])
                home_name, away_name = names.split('-')
                home_team_names_list.append(home_name)
                guest_team_names_list.append(away_name)
            except:
                try:
                    homeName, awayName = match['matchName'].split('·')
                    home_team_names_list.append(homeName)
                    guest_team_names_list.append(awayName)
                except:
                    home_team_names_list.append(match['matchName'])
                    guest_team_names_list.append('s')
    print('stigli dovde')
    i = 0
    for match_id in match_ids_list:
        match_odds = json_loading.get_odds_suberbet(match_id)

        # Flags to track if a list was updated during this match
        ki1_fulfilled = False
        ki2_fulfilled = False
        first_set_home_fulfilled = False
        first_set_away_fulfilled = False
        first_set_under_11_fulfilled = False
        first_set_11_or_over_fulfilled = False
        first_set_under_10_fulfilled = False
        first_set_10_or_over_fulfilled = False
        first_set_under_9_fulfilled = False
        first_set_9_or_over_fulfilled = False
        first_set_under_8_fulfilled = False
        first_set_8_or_over_fulfilled = False

        for match in match_odds["data"]:
            for odd in match['odds']:
                outcome_id = odd['outcomeId']
                special_value = odd.get('specialBetValue', None)

                if outcome_id == 1329:
                    ki1_list.append(odd['price'])
                    ki1_fulfilled = True
                elif outcome_id == 1330:
                    ki2_list.append(odd['price'])
                    ki2_fulfilled = True
                    if special_value == 1:
                        first_set_home_list.append(odd['price'])
                        first_set_home_fulfilled = True
                        first_set_away_list.append(odd['price'])
                        first_set_away_fulfilled = True
                elif outcome_id == 1335:
                    if special_value == '1-10.5':
                        first_set_under_11.append(odd['price'])
                        first_set_under_11_fulfilled = True
                    elif special_value == '1-9.5':
                        first_set_under_10.append(odd['price'])
                        first_set_under_10_fulfilled = True
                    elif special_value == '1-8.5':
                        first_set_under_9.append(odd['price'])
                        first_set_under_9_fulfilled = True
                    elif special_value == '1-7.5':
                        first_set_under_8.append(odd['price'])
                        first_set_under_8_fulfilled = True
                elif outcome_id == 1336:
                    if special_value == '1-10.5':
                        first_set_11_or_over.append(odd['price'])
                        first_set_11_or_over_fulfilled = True
                    elif special_value == '1-9.5':
                        first_set_10_or_over.append(odd['price'])
                        first_set_10_or_over_fulfilled = True
                    elif special_value == '1-8.5':
                        first_set_9_or_over.append(odd['price'])
                        first_set_9_or_over_fulfilled = True
                    elif special_value == '1-7.5':
                        first_set_8_or_over.append(odd['price'])
                        first_set_8_or_over_fulfilled = True
                else:
                    continue
        # After iterating through all odds for this match, append -1 if a list wasn't updated
            if not ki1_fulfilled:
                ki1_list.append(-1)
            if not ki2_fulfilled:
                ki2_list.append(-1)
            if not first_set_home_fulfilled:
                first_set_home_list.append(-1)
            if not first_set_away_fulfilled:
                first_set_away_list.append(-1)
            if not first_set_under_11_fulfilled:
                first_set_under_11.append(-1)
            if not first_set_11_or_over_fulfilled:
                first_set_11_or_over.append(-1)
            if not first_set_under_10_fulfilled:
                first_set_under_10.append(-1)
            if not first_set_10_or_over_fulfilled:
                first_set_10_or_over.append(-1)
            if not first_set_under_9_fulfilled:
                first_set_under_9.append(-1)
            if not first_set_9_or_over_fulfilled:
                first_set_9_or_over.append(-1)
            if not first_set_under_8_fulfilled:
                first_set_under_8.append(-1)
            if not first_set_8_or_over_fulfilled:
                first_set_8_or_over.append(-1)
    print('ipak ovde')
    headers = ["home_team", "away_team", "ki1", "ki2", "firstSet1", "firstSet2", "firstSet_u_10_5", "firstSet_o_11",
               "firstSet_u_9_5", "firstSet_o_10", "firstSet_u_8_5", "firstSet_o_9", "firstSet_u_7_5", "firstSet_o_8"]
    zipped = list(
        zip(home_team_names_list, guest_team_names_list, ki1_list,
            ki2_list, first_set_home_list, first_set_away_list, first_set_under_11, first_set_11_or_over,
            first_set_under_10, first_set_10_or_over, first_set_under_9, first_set_9_or_over,
            first_set_under_8, first_set_8_or_over))

    df = pd.DataFrame(zipped, columns=headers)
    df['ki1'] = df['ki1'].astype('float64')
    df['ki2'] = df['ki2'].astype('float64')
    df['firstSet1'] = df['firstSet1'].astype('float64')
    df['firstSet2'] = df['firstSet2'].astype('float64')
    df['firstSet_u_10_5'] = df['firstSet_u_10_5'].astype('float64')
    df['firstSet_u_9_5'] = df['firstSet_u_9_5'].astype('float64')
    df['firstSet_u_8_5'] = df['firstSet_u_8_5'].astype('float64')
    df['firstSet_u_7_5'] = df['firstSet_u_7_5'].astype('float64')
    df['firstSet_o_11'] = df['firstSet_o_11'].astype('float64')
    df['firstSet_o_10'] = df['firstSet_o_10'].astype('float64')
    df['firstSet_o_9'] = df['firstSet_o_9'].astype('float64')
    df['firstSet_o_8'] = df['firstSet_o_8'].astype('float64')

    return df


if __name__ == "__main__":
    s = json_loading.load_leagues_list_maxbet(
        'https://www.maxbet.rs/restapi/offer/sr/categories/sport/T/l?annex=3&desktopVersion=2.30.10&locale=sr')

    league_ids_list = []
    league_list = []
    for categorie in s['categories']:
        league_list.append(categorie['name'])
        league_ids_list.append(categorie['id'])

    home_team_names_list = []
    guest_team_names_list = []
    provider = []
    kickoff_time_list = []
    ki1_list = []
    ki2_list = []
    h1_list = []
    h2_list = []
    first_set_home_list = []
    first_set_away_list = []
    three_sets_list = []
    two_sets_list = []
    first_set_under_11 = []
    first_set_11_or_over = []
    first_set_under_10 = []
    first_set_10_or_over = []
    first_set_under_9 = []
    first_set_9_or_over = []
    first_set_under_8 = []
    first_set_8_or_over = []
    second_set_under_10 = []
    second_set_10_or_over = []
    second_set_under_9 = []
    second_set_9_or_over = []
    second_set_under_8 = []
    second_set_8_or_over = []
    matches_ids_list_df = []
    league_names_list = []


    for id in league_ids_list:
        f = json_loading.load_matches_list_maxbet(
            f'https://www.maxbet.rs/restapi/offer/sr/sport/T/league/{id}/mob?annex=3&desktopVersion=2.30.10&locale=sr')
        matches_ids_list = []

        for match in f['esMatches']:
            matches_ids_list.append(match['id'])
            matches_ids_list_df.append(match['id'])

        for match in matches_ids_list:
            a = json_loading.load_odds_maxbet(
                f'https://www.maxbet.rs/restapi/offer/sr/match/{match}?annex=3&desktopVersion=2.30.10&locale=sr')

            # if '/' in a['home']:
            #    parts = a['home'].split('/')
            #    try:
            #        e = json_loading.loadPlayerName(parts[0])
            #        r = json_loading.loadPlayerName(parts[1])
            #        home_team_names_list.append(e + "/" + r)
            #    except:
            #        home_team_names_list.append(a['home'])
            # elif '/' in a['away']:
            #    parts = a['home'].split('/')
            #    try:
            #        c = json_loading.loadPlayerName(parts[0])
            #        d = json_loading.loadPlayerName(parts[1])
            #        guest_team_names_list.append(c + "/" + d)
            #    except:
            #        guest_team_names_list.append(a['away'])
            # else:
            #    try:
            #        e = json_loading.loadPlayerName(a['home'])
            #        r = json_loading.loadPlayerName(a['away'])
            #        if e == 'Djokovic Marko':
            #            e = 'Djokovic Novak'
            #        elif r == 'Djokovic Marko':
            #            r = 'Djokovic Novak'
            #        home_team_names_list.append(e)
            #        guest_team_names_list.append(r)
            #    except:
            #        home_team_names_list.append(a['home'])
            #        guest_team_names_list.append(a['away'])
            try:
                result = json_loading.loadPlayerNameBasedOnMatch(a['home'] + '-' + a['away'])
                first_name, second_name = result.split('-')
                home_team_names_list.append(first_name)
                guest_team_names_list.append(second_name)
            except:
                home_team_names_list.append(a['home'])
                guest_team_names_list.append(a['away'])
            league_names_list.append(f['name'])

            timestamp_ms = a['kickOffTime']
            timestamp_s = timestamp_ms / 1000  # Convert milliseconds to seconds
            kick_off_time = datetime.datetime.utcfromtimestamp(timestamp_s)
            two_hours_addition = datetime.timedelta(hours=2)
            kick_off_time += two_hours_addition
            kickoff_time_list.append(kick_off_time)

            try:
                ki1_list.append(a['odds']['1'])
            except:
                ki1_list.append('-1')

            try:
                ki2_list.append(a['odds']['3'])
            except:
                ki2_list.append('-1')

            try:
                first_set_home_list.append(a['odds']['50512'])
            except:
                first_set_home_list.append('-1')

            try:
                first_set_away_list.append(a['odds']['50513'])
            except:
                first_set_away_list.append('-1')

            try:
                three_sets_list.append(a['odds']['261'])
            except:
                three_sets_list.append('-1')

            try:
                two_sets_list.append(a['odds']['260'])
            except:
                two_sets_list.append('-1')

            try:
                first_set_under_11.append(a['odds']['51373'])
            except:
                first_set_under_11.append('-1')

            try:
                first_set_11_or_over.append(a['odds']['51375'])
            except:
                first_set_11_or_over.append('-1')

            try:
                first_set_9_or_over.append(a['odds']['51372'])
            except:
                first_set_9_or_over.append('-1')

            try:
                first_set_under_9.append(a['odds']['51370'])
            except:
                first_set_under_9.append('-1')

            try:
                first_set_under_8.append(a['odds']['51376'])
            except:
                first_set_under_8.append('-1')

            try:
                first_set_8_or_over.append(a['odds']['51378'])
            except:
                first_set_8_or_over.append('-1')

            try:
                first_set_10_or_over.append(a['odds']['259'])
            except:
                first_set_10_or_over.append('-1')

            try:
                first_set_under_10.append(a['odds']['257'])
            except:
                first_set_under_10.append('-1')

            try:
                second_set_under_10.append(a['odds']['50520'])
            except:
                second_set_under_10.append('-1')

            try:
                second_set_10_or_over.append(a['odds']['50521'])
            except:
                second_set_10_or_over.append('-1')



            second_set_under_9.append('-1')
            second_set_9_or_over.append('-1')
            second_set_under_8.append('-1')
            second_set_8_or_over.append('-1')
            provider.append('MaxBet')
            h1_list.append('-1')
            h2_list.append('1')

    headers = ["provider", "kick_off", "league", "home_name", "away_name", "ki1", "ki2", "ts2", "ts3", "firstSet1",
               "firstSet2",
               "firstSet_u_10_5", "firstSet_o_11",
               "firstSet_u_9_5", "firstSet_o_10", "firstSet_u_8_5", "firstSet_o_9", "firstSet_u_7_5", "firstSet_o_8",
               "secondSet <9,5", "secondSet 10+", "secondSet <8,5", "secondSet 9+", "secondSet <7,5", "secondSet 8+"]

    zipped = list(
        zip(provider, kickoff_time_list, league_names_list, home_team_names_list, guest_team_names_list, ki1_list,
            ki2_list,
            two_sets_list,
            three_sets_list,
            first_set_home_list, first_set_away_list, first_set_under_11, first_set_11_or_over,
            first_set_under_10, first_set_10_or_over, first_set_under_9, first_set_9_or_over,
            first_set_under_8, first_set_8_or_over,
            second_set_under_10, second_set_10_or_over, second_set_under_9, second_set_9_or_over,
            second_set_under_8, second_set_8_or_over))

    df = pd.DataFrame(zipped, columns=headers)
    df['ki1'] = df['ki1'].astype('float64')
    df['ki2'] = df['ki2'].astype('float64')
    df['firstSet1'] = df['firstSet1'].astype('float64')
    df['firstSet2'] = df['firstSet2'].astype('float64')
    df['ts2'] = df['ts2'].astype('float64')
    df['ts3'] = df['ts3'].astype('float64')
    df['firstSet_u_10_5'] = df['firstSet_u_10_5'].astype('float64')
    df['firstSet_u_9_5'] = df['firstSet_u_9_5'].astype('float64')
    df['firstSet_u_8_5'] = df['firstSet_u_8_5'].astype('float64')
    df['firstSet_u_7_5'] = df['firstSet_u_7_5'].astype('float64')
    df['secondSet <9,5'] = df['secondSet <9,5'].astype('float64')
    df['secondSet <8,5'] = df['secondSet <8,5'].astype('float64')
    df['secondSet <7,5'] = df['secondSet <7,5'].astype('float64')
    df['firstSet_o_11'] = df['firstSet_o_11'].astype('float64')
    df['firstSet_o_10'] = df['firstSet_o_10'].astype('float64')
    df['firstSet_o_9'] = df['firstSet_o_9'].astype('float64')
    df['firstSet_o_8'] = df['firstSet_o_8'].astype('float64')
    df['secondSet 10+'] = df['secondSet 10+'].astype('float64')
    df['secondSet 9+'] = df['secondSet 9+'].astype('float64')
    df['secondSet 8+'] = df['secondSet 9+'].astype('float64')

    print(df.to_string())