
/*
 * CSCI3180 Principles of Programming Languages
 *
 * --- Declaration ---
 *
 * I declare that the assignment here submitted is original except for source
 * material explicitly acknowledged. I also acknowledge that I am aware of
 * University policy and regulations on honesty in academic work, and of the
 * disciplinary guidelines and procedures applicable to breaches of such policy
 * and regulations, as contained in the website
 * http://www.cuhk.edu.hk/policy/academichonesty/
 *
 * Assignment 2
 * Name : Wong Tsz Yin  
 * Student ID : 1155093245
 * Email Addr : 1155093245@link.cuhk.edu.hk
 */
public class Potion {
	private Pos pos;
	private int index;
	private String name;
	private int heal;
	protected Map map;
	int HEAL_CAP = 40;
	public Potion(int posx, int posy, int index, Map map) {
		this.map = map;
		this.pos = new Pos(posx, posy);
		this.index = index;
		this.name="P"+index;
		this.heal=TheJourney.rand.nextInt(HEAL_CAP) + 1;   
	}
         public boolean actionOnWarrior(Warrior warrior){
             int finalHeal=warrior.getHealth()+this.getHeal();
             //set heap_Cap
             if (finalHeal>HEAL_CAP)
                 finalHeal=HEAL_CAP;
             warrior.increaseHealth(finalHeal);
             warrior.talk("Very good, I got additional healing potion "+this.getName()+".");
             this.map.decreaseNumOfPotions();
             this.map.deleteTeleportableObj(this);
             return true;
         }
         
         public void teleport(){
             //find an unoccupiedpos to teleport
             this.map.setLand(this.pos, null);
             this.setPos(this.map.getUnOccupiedPosition());
             this.map.setLand(this.pos, this);
         }
         public int getHeal() {
			return heal;
		 }
         
         public String getName() {
			return name;
		}
        
         public void setPos(Pos pos) {
			this.pos = pos;
		} 
	
		public Pos getPos() {
			return this.pos;
		} 
         
}
