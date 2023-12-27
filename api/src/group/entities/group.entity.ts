import { LocationEntity } from 'src/location/entities/location.entity';
import { MessageEntity } from 'src/messages/entities/message.entity';
import {
  Column,
  Entity,
  OneToMany,
  OneToOne,
  PrimaryGeneratedColumn,
} from 'typeorm';

@Entity()
export class GroupEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true })
  link: string;

  @OneToOne(() => LocationEntity, (location) => location.group)
  location: LocationEntity;

  @OneToMany(() => MessageEntity, (message) => message.group)
  messages: MessageEntity[];
}
