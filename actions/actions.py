# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import cripto_bot
import crypto_terms

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAdicionarMoeda(Action):

    def name(self) -> Text:
        return "action_adicionar_moeda"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slot_value = tracker.get_slot('criptomoeda_nome')
        dispatcher.utter_message(text=f"{cripto_bot.add_favorites(slot_value)}")

        return []

class ActionConsultarCotacao(Action):

    def name(self) -> Text:
        return "action_consultar_cotacao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Certo, aqui está a cotação de suas moedas:")

        arr_favorite_coins = cripto_bot.consult_price()

        for currency in arr_favorite_coins:
            dispatcher.utter_message(text=f"{currency}")

        return []

class ActionConsultarTermos(Action):

    def name(self) -> Text:
        return "action_consultar_termos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slot_value = tracker.get_slot('criptomoeda_nome')
        dispatcher.utter_message(text=f"{crypto_terms.get_term(slot_value)}")

        return []
