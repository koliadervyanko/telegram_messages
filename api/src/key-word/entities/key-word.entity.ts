import { MessageEntity } from 'src/messages/entities/message.entity';
import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class KeyWordEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true })
  keyWord: string;

  @OneToMany(() => MessageEntity, (message) => message.keyWord)
  messages: MessageEntity[];
}
