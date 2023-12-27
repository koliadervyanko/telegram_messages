import { Injectable, InternalServerErrorException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { KeyWordEntity } from './entities/key-word.entity';
import { Repository } from 'typeorm';

@Injectable()
export class KeyWordService {
  constructor(
    @InjectRepository(KeyWordEntity)
    private repository: Repository<KeyWordEntity>,
  ) {}
  findAll() {
    return `This action returns all keyWord`;
  }
  async findOne(keyWord: string) {
    try {
      const entity = await this.repository.findOneBy({ keyWord });
      return entity;
    } catch (error) {
      throw new InternalServerErrorException(`Error: ${error}`);
    }
  }
}
