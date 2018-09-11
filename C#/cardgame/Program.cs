using System;
using System.Collections.Generic;
namespace cardgame
{
    public class Card
    {
        public int val;
        public string suit;
        public Card(int value, string suite)
        {
            val = value;
            suit = suite;
        }
    }
    public class Deck
    {
        public List<Card> cards;
        public Deck()
        {
            reset();
            shuffle();
        }
        public Deck reset()
        {
            string[] suits = { "heart", "diamond", "spade", "club" };
            cards = new List<Card>();
            for (int i = 0; i < suits.Length; i++)
            {
                for(int j = 1; j < 14; j++)
                {
                    cards.Add(new Card(j, suits[i]));
                }
            }
            return this;
        }
        public Deck shuffle()
        {
            Random rand = new Random();
            for (int i = 0; i < cards.Count; i++)
            {
                int ran = rand.Next(cards.Count);
                Card tmp = cards[i];
                cards[i] = cards[ran];
                cards[ran] = tmp;
            }
            return this;
        }
        public Card deal()
        {
            if (cards.Count > 0)
            {
                Card res = cards[0];
                cards.RemoveAt(0);
                return res;
            }
            else
            {
                reset();
                return deal();
            }
        }
    }
    public class Player
    {
        public string[] name;
        public List<Card> hand;
        public List<Card> draw(Deck deck)
        {
            if (deck.cards.Count > 0)
            {
                Card res = deck.cards[0];
                deck.cards.RemoveAt(0);
                hand.Add(res);
                return hand;
            }
            else 
            {
                deck.reset();
                return draw(deck);
            }
        }
        public Card discard(List<Card> hand, int i)
        {
            if(hand[i] != null)
            {
                Card res = hand[i];
                hand.RemoveAt(i);
                return res;
            }
            else
            {
                return null;
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            var deck = new Deck();
            Console.WriteLine(deck.cards);
        }
    }
}
